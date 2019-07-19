from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import backend

# noinspection PyArgumentList
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(777, 379)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.calculate = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculate.sizePolicy().hasHeightForWidth())
        self.calculate.setSizePolicy(sizePolicy)
        self.calculate.setObjectName("calculate")
        self.gridLayout.addWidget(self.calculate, 1, 0, 1, 1)
        self.upload = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload.sizePolicy().hasHeightForWidth())
        self.upload.setSizePolicy(sizePolicy)
        self.upload.setObjectName("upload")
        self.gridLayout.addWidget(self.upload, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gpa_header = QtWidgets.QLabel(Dialog)
        self.gpa_header.setObjectName("gpa_header")
        self.verticalLayout.addWidget(self.gpa_header)
        self.gpa_display = QtWidgets.QLabel(Dialog)
        self.gpa_display.setObjectName("gpa_display")
        self.verticalLayout.addWidget(self.gpa_display)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.course_filter = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.course_filter.sizePolicy().hasHeightForWidth())
        self.course_filter.setSizePolicy(sizePolicy)
        self.course_filter.setObjectName("course_filter")
        self.verticalLayout_2.addWidget(self.course_filter)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.course_filter_options = QtWidgets.QComboBox(self.frame_3)
        self.course_filter_options.setObjectName("course_filter_options")
        self.horizontalLayout_2.addWidget(self.course_filter_options)
        self.label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.course_filter_options_2 = QtWidgets.QComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.course_filter_options_2.sizePolicy().hasHeightForWidth())
        self.course_filter_options_2.setSizePolicy(sizePolicy)
        self.course_filter_options_2.setCurrentText("")
        self.course_filter_options_2.setFrame(True)
        self.course_filter_options_2.setObjectName("course_filter_options_2")
        self.horizontalLayout_2.addWidget(self.course_filter_options_2)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.course_num_filter = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.course_num_filter.sizePolicy().hasHeightForWidth())
        self.course_num_filter.setSizePolicy(sizePolicy)
        self.course_num_filter.setObjectName("course_num_filter")
        self.verticalLayout_2.addWidget(self.course_num_filter)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.course_level_options = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.course_level_options.sizePolicy().hasHeightForWidth())
        self.course_level_options.setSizePolicy(sizePolicy)
        self.course_level_options.setObjectName("course_level_options")
        self.horizontalLayout.addWidget(self.course_level_options)
        spacerItem = QtWidgets.QSpacerItem(13, 5, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.course_number_textentry = QtWidgets.QTextEdit(self.frame_2)
        self.course_number_textentry.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.course_number_textentry.sizePolicy().hasHeightForWidth())
        self.course_number_textentry.setSizePolicy(sizePolicy)
        self.course_number_textentry.setMinimumSize(QtCore.QSize(0, 25))
        self.course_number_textentry.setAcceptDrops(True)
        self.course_number_textentry.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.course_number_textentry.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.course_number_textentry.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.course_number_textentry.setObjectName("course_number_textentry")
        self.horizontalLayout.addWidget(self.course_number_textentry)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.credit_options = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_options.sizePolicy().hasHeightForWidth())
        self.credit_options.setSizePolicy(sizePolicy)
        self.credit_options.setObjectName("credit_options")
        self.horizontalLayout_3.addWidget(self.credit_options)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.credit_number_textentry = QtWidgets.QTextEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_number_textentry.sizePolicy().hasHeightForWidth())
        self.credit_number_textentry.setSizePolicy(sizePolicy)
        self.credit_number_textentry.setMinimumSize(QtCore.QSize(0, 25))
        self.credit_number_textentry.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.credit_number_textentry.setObjectName("credit_number_textentry")
        self.horizontalLayout_3.addWidget(self.credit_number_textentry)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.semester_filter = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semester_filter.sizePolicy().hasHeightForWidth())
        self.semester_filter.setSizePolicy(sizePolicy)
        self.semester_filter.setObjectName("semester_filter")
        self.verticalLayout_2.addWidget(self.semester_filter)
        self.semester_filter_options = QtWidgets.QComboBox(self.frame)
        self.semester_filter_options.setObjectName("semester_filter_options")
        self.verticalLayout_2.addWidget(self.semester_filter_options)
        self.year_filter = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year_filter.sizePolicy().hasHeightForWidth())
        self.year_filter.setSizePolicy(sizePolicy)
        self.year_filter.setObjectName("year_filter")
        self.verticalLayout_2.addWidget(self.year_filter)
        self.year_filter_options = QtWidgets.QComboBox(self.frame)
        self.year_filter_options.setObjectName("year_filter_options")
        self.verticalLayout_2.addWidget(self.year_filter_options)
        self.gridLayout.addWidget(self.frame, 0, 1, 3, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.calculate.setEnabled(False)

        if backend.check_connection():
            self.calculate.setEnabled(True)
            self.setup_GUI()

        self.upload.clicked.connect(self.connection_handler)
        self.calculate.clicked.connect(self.set_gpa)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.calculate.setText(_translate("Dialog", "CALCULATE"))
        self.upload.setText(_translate("Dialog", "UPLOAD"))
        self.gpa_header.setText(_translate("Dialog", "GPA:"))
        self.gpa_display.setText(_translate("Dialog", "TextLabel"))
        self.course_filter.setText(_translate("Dialog", "Courses"))
        self.label.setText(_translate("Dialog", "OR"))
        self.course_num_filter.setText(_translate("Dialog", "Course Level"))
        self.course_number_textentry.setPlaceholderText(_translate("Dialog", "Course Number"))
        self.label_2.setText(_translate("Dialog", "Credits"))
        self.credit_number_textentry.setPlaceholderText(_translate("Dialog", "Credits"))
        self.semester_filter.setText(_translate("Dialog", "Semester"))
        self.year_filter.setText(_translate("Dialog", "Year"))

    # Get the user to select the pdf copy of their transcript, need to develop a function to validate the input
    def connection_handler(self):

        file, _ = QFileDialog.getOpenFileNames(None, "", "Transcript", ".pdf (*.pdf)")
        if file:  # TODO implement validity check (MAKE SURE PDF IS CORRECT DOCUMENT TYPE)

            backend.create_data_connection(file[0])
            self.calculate.setEnabled(True)
            self.setup_GUI()

    # Populate all filter fields with backend data
    def setup_GUI(self):

        self.course_level_options.addItems(["----", "Exactly Equals", "Greater Than", "Less Than"])
        self.credit_options.addItems(["----", "First X Credits", "Last X Credits"])

        filter_options = backend.generate_filtering_options()
        self.course_filter_options.addItems(filter_options[0])
        self.course_filter_options_2.addItems(filter_options[0])
        self.year_filter_options.addItems(filter_options[1])
        self.semester_filter_options.addItems(filter_options[2])

    # Pass filter information to backend to build query (after input validity is checked), and display the result of
    # executing the query, the GPA!
    def set_gpa(self):

        valid_input = self.input_validation()

        if valid_input == 0:
            # Get all filter information from the frontend and pass it to the backend
            fi = [[self.course_filter_options.currentText(), self.course_filter_options_2.currentText()],  # Subject titles
                  [self.course_level_options.currentText(), self.course_number_textentry.toPlainText()],  # Course number
                  [self.credit_options.currentText(), self.credit_number_textentry.toPlainText()],  # Credit values
                  [self.semester_filter_options.currentText()],  # Semester values
                  [self.year_filter_options.currentText()]]  # Year values

            self.gpa_display.setText(backend.calculate_gpa(fi))

        elif valid_input == 1:
            error_message = QtWidgets.QMessageBox()
            error_message.about(error_message, "Input Error", "Course number must be a 3 digit number!")

        elif valid_input == 2:
            error_message = QtWidgets.QMessageBox()
            error_message.about(error_message, "Test", "Input Error", "Credit value must be a 1-3 digit number!")

    # Ensures course_num and credit_num are proper text options, otherwise return a code that will create an error dialog
    def input_validation(self):
        course_num = self.course_number_textentry.toPlainText()
        credit_count = self.credit_number_textentry.toPlainText()

        if self.course_level_options.currentText() != '----':
            print(self.course_level_options.currentText())
            if not(len(course_num) == 3 and course_num.isdigit()):
                return 1
        elif self.credit_options.currentText() != '----':
            print(self.credit_options.currentText())
            if not(1 <= len(credit_count) < 4 and course_num.isdigit()):
                return 2

        return 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
