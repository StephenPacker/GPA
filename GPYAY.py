# GPYAY is a simple terminal based prototype, the more advanced and feature filled versions are backend and gui

import io
import sqlite3

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def main():
    db_con = create_database()
    text = (extract_text_from_pdf('transcript.pdf')).split(" ")
    cleaned_text = clean_text(text)
    build_data_table(cleaned_text, db_con)
    calculate_gpa(db_con)


def create_database():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    try:
        cursor.execute("DROP TABLE transcript")
    except sqlite3.OperationalError:
        pass

    create_schema = "CREATE TABLE transcript (subject text, coursenum int, grade float, year int, sem text);"
    cursor.execute(create_schema)

    return con


# Taken from: http://www.blog.pythonlibrary.org/2018/05/03/exporting-data-from-pdfs-with-python/
# Syntax to extract text from a pdf. Returned as a single string. Currently assumes the correct pdf is provided.
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

    return text


# Cleans the text for processing including removing white spaces and ensuring all courses titles are properly split.
def clean_text(text):

    # Removes white spaces
    text = [x for x in text if x != ""]

    for i in range(0, len(text) - 1):

        # Handles the case where a courses title gets combined with an int (i.e 66EAS)
        if any(char.isdigit() for char in text[i]) and any(char.isalpha() for char in text[i]):
            word = text[i]
            for j in range(0, len(word) - 1):
                if word[j].isdigit() and word[j + 1].isalpha():
                    text[i] = word[j + 1:]

        # Handles the case where a courses title gets combined with another word int (i.e EnrolledCMPUT)
        elif 2 <= len([char for char in text[i] if char.isupper()]) < len(text[i]):  # Mixed upper and lower case
            word = text[i]
            for j in range(0, len(word) - 1):
                if word[j].islower() and word[j + 1].isupper():
                    text[i] = word[j + 1:]

        # TODO NEEDS TO BE TESTED
        # Handles the case of split course titles i.e B LAW, CIV E, HE ED
        if 3 <= len(text[i]) + len(text[i + 1]) < 6 and text[i].isupper() and text[i + 1].isupper() and text[i + 2].isdigit():
            text[i] = text[i] + text[i + 1]
            text[i + 1] = "VOID"  # Because we cant modify list in loop, set flags to be removed during final list clean

    return [x for x in text if x != "VOID"]


# Extract all information form the pdf and store it in a data table for easier querying in future operations.
# Each course will have semester, year, course type, number and grade, allowing for better filtering operations.
def build_data_table(text, db_con):

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

        # Ensure I get the correct course type before creating a new table entry
        elif 3 <= len(text[i]) < 6 and text[i].isupper() and text[i][-1] != ":" and text[i + 1][0].isdigit():
            j = i + 2
            grade = None
            while not grade:  # Once we know we have a course, get the number and the grade before creating a entry
                if text[j][0].isdigit() and 4 <= len(text[j]) < 6:
                    insert_sql = "INSERT INTO transcript (subject, coursenum, grade, year, sem) VALUES (?,?,?,?,?);"
                    cursor.execute(insert_sql, (text[i], text[i + 1], text[j], semester, year))
                    # courses.append([text[i], text[i + 1], text[j], semester, year])
                    grade = True
                    i = j
                elif text[j] == 'W': # Ignore withdrawn courses
                    grade = True
                else:
                    j += 1
        i += 1

        db_con.commit()


# Simple gpa calculator system
def calculate_gpa(db_con):

    cursor = db_con.cursor()
    cursor.execute("SELECT AVG(grade)/3 FROM transcript WHERE subject = 'EAS'")
    print(cursor.fetchone())

    # cursor = db_con.cursor()
    # cursor.execute("SELECT subject, coursenum FROM transcript ORDER BY grade ASC")
    #
    # for course in enumerate(cursor.fetchall()):
    #     print(course)


main()

