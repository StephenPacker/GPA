# Written by Stephen Packer in July 2019.
# Backend for GPYAY application, a simple desktop application that allows students to quickly calculate GPA using a
# variety of filters. The backend handles all interactions with the data, including reading the transcript to create the
# source data, providing information to the front end in terms of filter options, and executing queries on the data.

# NOTE: This program is not designed to read transcripts of a different format. Specifically, the functions clean_text and
# build_data_table use pattern matching specifically for the U of A transcript to extract the key information. Outside
# of these two functions, everything should be generic to any transcript. Thus if someone wanted to edit the program for
# another institution hopefully modifying these two functions should suffice.

import io
import sqlite3
import os.path

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

db_con = None
credit_query = None		# Special case handling for credit queries, simpler to do data processing in python vs sql


# Check if a data connection already exists and if so connect to immediately, allowing the user to skip the re-uploading
# of transcripts each time. If no connection exists, returns false and users will have to upload a transcript to proceed.
def check_connection():
	global db_con

	if os.path.exists("data.db"):
		db_con = sqlite3.connect("data.db")
		return True
	else:
		return False


# Facilitates the creation of the data table, including creating the database schema, extracting and cleaning information
# from the pdf transcript and finally inserting it into the database.
def create_data_connection(file):

	create_database()
	text = (extract_text_from_pdf(file))
	cleaned_text = clean_text(text)
	build_data_table(cleaned_text)


# Create database schema and the connection to the database if one does not exist
def create_database():
	global db_con

	db_con = sqlite3.connect("data.db")
	cursor = db_con.cursor()

	try:
		cursor.execute("DROP TABLE transcript")
	except sqlite3.OperationalError:
		pass

	create_schema = "CREATE TABLE transcript (subject text, coursenum int, grade float, year int, sem text, credit int);"
	cursor.execute(create_schema)


# Taken from: http://www.blog.pythonlibrary.org/2018/05/03/exporting-data-from-pdfs-with-python/
# Code to extract text from a pdf using pdfminer. Returned as a single string.
def extract_text_from_pdf(pdf_path):
	resource_manager = PDFResourceManager()
	fake_file_handle = io.StringIO()
	converter = TextConverter(resource_manager, fake_file_handle)
	page_interpreter = PDFPageInterpreter(resource_manager, converter)

	with open(pdf_path, 'rb') as fh:
		for page in PDFPage.get_pages(fh, caching=True, check_extractable=False):
			page_interpreter.process_page(page)
		text = fake_file_handle.getvalue()

	converter.close()
	fake_file_handle.close()

	return text.split(" ")  # Return a list of words instead of a single string


# Cleans the text for processing including removing white spaces and ensuring all courses titles are properly split.
def clean_text(text):
	# Removes white spaces
	text = [x for x in text if x != ""]

	for i in range(0, len(text) - 1):

		# Handles the case where a courses title gets combined with an int (i.e 66EAS)
		if any(char.isdigit() for char in text[i]) and any(char.isalpha() for char in text[i]):  # Mixed ints and text
			word = text[i]
			for j in range(0, len(word) - 1):
				if word[j].isdigit() and word[j + 1].isalpha():
					text[i] = word[j + 1:]

		# Handles the case where a courses title gets combined with another word (i.e EnrolledCMPUT)
		elif 2 <= len([char for char in text[i] if char.isupper()]) < len(text[i]):  # Mixed upper and lower case
			word = text[i]
			for j in range(0, len(word) - 1):
				if word[j].islower() and word[j + 1].isupper():
					text[i] = word[j + 1:]

		# TODO NEEDS TO BE TESTED MORE THOROUGHLY
		# Handles the case of split course titles i.e B LAW, CIV E, HE ED
		if 3 <= len(text[i]) + len(text[i + 1]) < 6 and text[i].isupper() and text[i + 1].isupper() and text[
			i + 2].isdigit():
			text[i] = text[i] + text[i + 1]
			text[i + 1] = "VOID"  # Because we cant modify list in loop, set flags to be removed during final list clean

	return [x for x in text if x != "VOID"]


# Extract all information form the pdf and store it in a data table for easier querying in future operations.
# Each course will have semester, year, course type, number and grade, allowing for better filtering operations.
def build_data_table(text):
	# Set up variables
	year = ""
	semester = ""
	semesters = ["Fall", "Winter", "Summer", "Spring"]
	cursor = db_con.cursor()

	i = 0

	while i < len(text):

		if len(text[i]) == 4 and text[i].isdigit():  # Get the current year
			year = text[i]

		elif text[i] in semesters:  # Get the current semester
			semester = text[i]

		# Main text extraction algorithm. Based heavily on pattern matching the U of A transcript format. Once we find
		# A course title (the below elif clause), we begin extracting all the other metadata. The format is as follows:

		# Course - Course Number - Description - Letter Grade - Course Credits - Credits Earned - Grade (0-12) - Class Avg - Enrollment
		#  CMPUT        204        ALGORITHMS 1       A               3.0               3.0           12.00          2.8         86

		elif 3 <= len(text[i]) < 6 and text[i].isupper() and text[i][-1] != ":" and text[i + 1][0].isdigit():
			j = i + 4  # Try to skip unused info (course description, possibly letter grade, credits if short description)
			grade = None
			while not grade:  # Find the grade which is always a float between 4 and 5 chars, used as the anchor point
				if text[j][0].isdigit() and 4 <= len(text[j]) < 6:  # Once found, insert entry into the database
					insert_sql = "INSERT INTO transcript (subject, coursenum, grade, year, sem, credit) VALUES (?,?,?,?,?,?);"
					cursor.execute(insert_sql, (text[i], text[i + 1], text[j], year, semester, text[j - 2]))
					grade = True
					i = j + 1  # Skip class avg and enrollment and to expedite process
				elif text[j] == 'W':  # Ignore withdrawn courses
					grade = True
				else:
					j += 1

		i += 1

		db_con.commit()  # Commit data to the database


# Called by the frontend to produce the filtering options that will be displayed in the drop downs (adaptive UI!)
def generate_filtering_options():
	cursor = db_con.cursor()

	# Generate all courses a user can filter through
	cursor.execute("SELECT DISTINCT subject FROM transcript GROUP BY subject ORDER BY COUNT(*) DESC")
	subjects = [x[0] for x in cursor.fetchall()]
	subjects.insert(0, "----")

	# Generate all years a user can filter through
	cursor.execute("SELECT DISTINCT year FROM transcript")
	years = [str(x[0]) for x in cursor.fetchall()]
	years.insert(0, "----")

	# Generate all semester a user can filter through
	cursor.execute("SELECT DISTINCT sem FROM transcript")
	semesters = [x[0] for x in cursor.fetchall()]
	semesters.insert(0, "----")

	return subjects, years, semesters


# Simple gpa calculator system, calls the query builder and executes and returns its results
def calculate_gpa(query_information):
	cursor = db_con.cursor()
	query = query_builder(query_information)

	# Credit queries have special handling because we need to return the first or last n results based on user input.
	if credit_query:
		gpa = execute_credit_query(query, query_information[2][1])
	else:
		# print(query) FOR TESTING ID QUERIES ARE PROPERLY BUILT
		cursor.execute(query)
		gpa = str(cursor.fetchone()[0])

	return gpa


# Given the user input in the frontend builds the corresponding query. Query information is a list containing all the
# user information (subject, course number, credit, semester, year) in that order.
def query_builder(query_information):
	global credit_query

	root = "SELECT AVG(grade)/3 FROM transcript"  # Standard query if no filters are selected (considers all courses)

	if [x for x in query_information if x[0] != "----"]:  # Check if any filter options have been selected
		query = root + " WHERE "

		# Queries related to subject names
		if query_information[0][0] != "----" and query_information[0][1] != "----":
			query = query + "subject = '%s' OR subject = '%s' AND " % (query_information[0][0], query_information[0][1])
		elif query_information[0][0] != "----":
			query = query + "subject = '%s' AND " % query_information[0][0]

		# Related to course number
		if query_information[1][0] == "Exactly Equals" and query_information[1][1] != "":
			query = query + "coursenum = %i AND " % (int(query_information[1][1]))
		elif query_information[1][0] == "Greater Than" and query_information[1][1] != "":
			query = query + "coursenum > %i AND " % (int(query_information[1][1]))
		elif query_information[1][0] == "Less Than" and query_information[1][1] != "":
			query = query + "coursenum < %i AND " % (int(query_information[1][1]))

		# Related to credits requirements (Just sets flags, which if set will trigger a more in depth function for credit queries)
		if query_information[2][0] != "----" and query_information[2][1] != "":
			if query_information[2][0] == "First X Credits":
				credit_query = "First"
			elif query_information[2][0] == "Last X Credits":
				credit_query = "Last"

		# Related to sem queries
		if query_information[3][0] != "----":
			query = query + "sem = '%s' AND " % query_information[3][0]

		# Related to year queries
		if query_information[4][0] != "----":
			query = query + "year = '%s' AND " % query_information[4][0]

		return query[0:-5]  # All queries have a trailing AND so this filters it out

	else:  # Return the unaltered query
		return root


# Specific handling for credit queries, modifies root query to return grade/credit of all courses which is then sliced
# to return GPA of last/first N credits. Necessary because courses can have a variable amount of credits, cant assume
# taking the top 10 is valid. (POSSIBLY REFACTOR TO DO DATA PROCESSING ALL IN SQL)
def execute_credit_query(query, credit_amount):
	cursor = db_con.cursor()

	# Alter the first part of the query so it returns all results instead of gpa.
	for i in range(0, len(query)):
		if query[i] == "F":  # Look for the FROM keyword, and this is where I will split the OG query
			right_query_side = query[i:]
			left_query_side = "SELECT grade, credit "
			new_query = left_query_side + right_query_side

	# print(new_query) FOR TESTING ID QUERIES ARE PROPERLY BUILT
	cursor.execute(new_query)
	results = cursor.fetchall()

	if credit_query == "Last":
		results.reverse()

	credit_sum = 0
	grades_sum = 0
	course_count = 0
	while credit_sum < int(credit_amount) and course_count < len(results):
		grades_sum += results[course_count][0]/3
		credit_sum += results[course_count][1]
		course_count += 1

	return str(grades_sum/course_count)

