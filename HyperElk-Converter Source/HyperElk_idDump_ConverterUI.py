import os
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QGridLayout, QPushButton, QLabel


class UiMainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 453)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 290, 801, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layout_button_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout_button_grid.setContentsMargins(0, 0, 0, 0)
        self.layout_button_grid.setObjectName("layout_button_grid")
        self.sign_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sign_button.setObjectName("sign_button")
        self.layout_button_grid.addWidget(self.sign_button, 3, 4, 1, 1)
        self.spell_name_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.spell_name_button.setObjectName("spell_name_button")
        self.layout_button_grid.addWidget(self.spell_name_button, 2, 0, 1, 1)
        self.protected_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.protected_button.setObjectName("protected_button")
        self.layout_button_grid.addWidget(self.protected_button, 2, 2, 1, 1)
        self.talent_id_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.talent_id_button.setObjectName("talent_id_button")
        self.layout_button_grid.addWidget(self.talent_id_button, 3, 1, 1, 1)
        self.structure_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.structure_button.setObjectName("structure_button")
        self.layout_button_grid.addWidget(self.structure_button, 3, 5, 1, 1)
        self.var_talent_name_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.var_talent_name_button.setObjectName("var_talent_name_button")
        self.layout_button_grid.addWidget(self.var_talent_name_button, 1, 1, 1, 1)
        self.new_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.new_button.setObjectName("new_button")
        self.layout_button_grid.addWidget(self.new_button, 1, 4, 1, 1)
        self.int_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.int_button.setObjectName("int_button")
        self.layout_button_grid.addWidget(self.int_button, 3, 3, 1, 1)
        self.spell_id_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.spell_id_button.setObjectName("spell_id_button")
        self.layout_button_grid.addWidget(self.spell_id_button, 3, 0, 1, 1)
        self.static_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.static_button.setObjectName("static_button")
        self.layout_button_grid.addWidget(self.static_button, 1, 3, 1, 1)
        self.TalentTalent_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.TalentTalent_button.setObjectName("TalentTalent_button")
        self.layout_button_grid.addWidget(self.TalentTalent_button, 1, 5, 1, 1)
        self.talent_name_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.talent_name_button.setObjectName("talent_name_button")
        self.layout_button_grid.addWidget(self.talent_name_button, 2, 1, 1, 1)
        self.SpellSpellButton: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SpellSpellButton.setObjectName("SpellSpellButton")
        self.layout_button_grid.addWidget(self.SpellSpellButton, 2, 5, 1, 1)
        self.var_spell_name_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.var_spell_name_button.setObjectName("var_spell_name_button")
        self.layout_button_grid.addWidget(self.var_spell_name_button, 1, 0, 1, 1)
        self.class_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.class_button.setObjectName("class_button")
        self.layout_button_grid.addWidget(self.class_button, 2, 4, 1, 1)
        self.bool_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bool_button.setObjectName("bool_button")
        self.layout_button_grid.addWidget(self.bool_button, 2, 3, 1, 1)
        self.private_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.private_button.setObjectName("private_button")
        self.layout_button_grid.addWidget(self.private_button, 1, 2, 1, 1)
        self.public_button: QPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.public_button.setObjectName("public_button")
        self.layout_button_grid.addWidget(self.public_button, 3, 2, 1, 1)
        self.layout_vert_path = QtWidgets.QWidget(self.centralwidget)
        self.layout_vert_path.setGeometry(QtCore.QRect(10, 10, 801, 91))
        self.layout_vert_path.setObjectName("layout_vert_path")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layout_vert_path)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(1, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_input_path = QtWidgets.QLabel(self.layout_vert_path)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_input_path.setFont(font)
        self.label_input_path.setAutoFillBackground(True)
        self.label_input_path.setObjectName("label_input_path")
        self.gridLayout_2.addWidget(self.label_input_path, 1, 0, 1, 1)
        self.label_output_path: QLabel = QtWidgets.QLabel(self.layout_vert_path)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_output_path.setFont(font)
        self.label_output_path.setAutoFillBackground(True)
        self.label_output_path.setObjectName("label_output_path")
        self.gridLayout_2.addWidget(self.label_output_path, 3, 0, 1, 1)
        self.InputLineEdit = QtWidgets.QLineEdit(self.layout_vert_path)
        self.InputLineEdit.setAutoFillBackground(False)
        self.InputLineEdit.setObjectName("InputLineEdit")
        self.gridLayout_2.addWidget(self.InputLineEdit, 1, 3, 1, 1)
        # Input browse-button
        self.input_browse_button: QPushButton = QtWidgets.QPushButton(self.layout_vert_path)
        self.input_browse_button.setObjectName("input_browse_button")
        self.gridLayout_2.addWidget(self.input_browse_button, 1, 2, 1, 1)
        # Output browse-button
        self.output_browse_button: QPushButton = QtWidgets.QPushButton(self.layout_vert_path)
        self.output_browse_button.setDefault(False)
        self.output_browse_button.setFlat(False)
        self.output_browse_button.setObjectName("output_browse_button")
        self.gridLayout_2.addWidget(self.output_browse_button, 3, 2, 1, 1)
        # Output Line Edit
        self.OutputLineEdit = QtWidgets.QLineEdit(self.layout_vert_path)
        self.OutputLineEdit.setObjectName("OutputLineEdit")
        self.gridLayout_2.addWidget(self.OutputLineEdit, 3, 3, 1, 1)
        # Vertical Layout Widget
        self.verticalLayoutWidget: QtWidgets = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 801, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # Process Button
        self.process_button: QPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.process_button.setObjectName("process_button")
        # Input Text Box
        self.verticalLayout.addWidget(self.process_button)
        self.InputTextBox = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputTextBox.sizePolicy().hasHeightForWidth())
        self.InputTextBox.setSizePolicy(sizePolicy)
        self.InputTextBox.setObjectName("InputTextBox")
        self.verticalLayout.addWidget(self.InputTextBox)

        self.process_button.clicked.connect(lambda: self.process_files())
        self.input_browse_button.clicked.connect(lambda: self.browse_input())
        self.output_browse_button.clicked.connect(lambda: self.browse_output())
        self.var_spell_name_button.clicked.connect(lambda: self.insert_text("{var_spell_name}"))
        self.spell_name_button.clicked.connect(lambda: self.insert_text("{spell_name}"))
        self.spell_id_button.clicked.connect(lambda: self.insert_text("{spell_id}"))
        self.var_talent_name_button.clicked.connect(lambda: self.insert_text("{var_talent_name}"))
        self.talent_name_button.clicked.connect(lambda: self.insert_text("{talent_name}"))
        self.talent_id_button.clicked.connect(lambda: self.insert_text("{talent_id}"))
        self.private_button.clicked.connect(lambda: self.insert_text("private "))
        self.protected_button.clicked.connect(lambda: self.insert_text("protected "))
        self.public_button.clicked.connect(lambda: self.insert_text("public "))
        self.static_button.clicked.connect(lambda: self.insert_text("static "))
        self.bool_button.clicked.connect(lambda: self.insert_text("bool "))
        self.int_button.clicked.connect(lambda: self.insert_text("int "))
        self.new_button.clicked.connect(lambda: self.insert_text("new "))
        self.class_button.clicked.connect(lambda: self.insert_text("class "))
        self.sign_button.clicked.connect(lambda: self.insert_text("("",);"))
        self.TalentTalent_button.clicked.connect(lambda: self.insert_text("Talent.{var_talent_name}"))
        self.SpellSpellButton.clicked.connect(lambda: self.insert_text("Spell.{var_spell_name}"))
        self.structure_button.clicked.connect(lambda: self.insert_text("public class {}"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.public_button, self.talent_id_button)
        MainWindow.setTabOrder(self.talent_id_button, self.talent_name_button)
        MainWindow.setTabOrder(self.talent_name_button, self.var_talent_name_button)
        MainWindow.setTabOrder(self.var_talent_name_button, self.var_spell_name_button)
        MainWindow.setTabOrder(self.var_spell_name_button, self.SpellSpellButton)
        MainWindow.setTabOrder(self.SpellSpellButton, self.protected_button)
        MainWindow.setTabOrder(self.protected_button, self.spell_name_button)
        MainWindow.setTabOrder(self.spell_name_button, self.bool_button)
        MainWindow.setTabOrder(self.bool_button, self.structure_button)
        MainWindow.setTabOrder(self.structure_button, self.private_button)
        MainWindow.setTabOrder(self.private_button, self.spell_id_button)
        MainWindow.setTabOrder(self.spell_id_button, self.int_button)
        MainWindow.setTabOrder(self.int_button, self.TalentTalent_button)
        MainWindow.setTabOrder(self.TalentTalent_button, self.static_button)

    def hide_talents_buttons(self):
        # Hiding Talents if a Spell File is selected to void runtime errors
        self.TalentTalent_button.hide()
        self.talent_id_button.hide()
        self.talent_name_button.hide()
        self.var_talent_name_button.hide()
        self.SpellSpellButton.show()
        self.spell_id_button.show()
        self.spell_name_button.show()
        self.var_spell_name_button.show()

    def hide_spells_buttons(self):
        # Hiding Spells if a Talent File is selected to void runtime errors
        self.SpellSpellButton.hide()
        self.spell_id_button.hide()
        self.spell_name_button.hide()
        self.var_spell_name_button.hide()
        self.TalentTalent_button.show()
        self.talent_id_button.show()
        self.talent_name_button.show()
        self.var_talent_name_button.show()

    def browse_input(self):
        # Browse Input function.
        # Copy the selected File's Path to both Input and Output path
        # Output-path gets modified to create a non-typeless file
        file_path, _ = QFileDialog.getOpenFileName()
        if file_path:
            self.InputLineEdit.setText(file_path)
            notype = (file_path.split(".")[0])
            tyoeoffile = os.path.basename(file_path).split('.')[1]
            self.OutputLineEdit.setText(notype + "-output." + tyoeoffile)
            talentsorspells = os.path.basename(file_path).split('.')[0]
            if talentsorspells == "Spells":
                self.hide_talents_buttons()
            if talentsorspells == "Talents":
                self.hide_spells_buttons()

    def retranslateUi(self, MainWindow):
        # QT generated Code for translation
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sign_button.setText(_translate("MainWindow", "(\"\", );"))
        self.spell_name_button.setText(_translate("MainWindow", "Spell Name"))
        self.protected_button.setText(_translate("MainWindow", "protected"))
        self.talent_id_button.setText(_translate("MainWindow", "Talent ID"))
        self.structure_button.setText(_translate("MainWindow", "STRUCTURE"))
        self.var_talent_name_button.setText(_translate("MainWindow", "Var:Talent Name"))
        self.new_button.setText(_translate("MainWindow", "new"))
        self.int_button.setText(_translate("MainWindow", "int"))
        self.spell_id_button.setText(_translate("MainWindow", "Spell ID"))
        self.static_button.setText(_translate("MainWindow", "static"))
        self.TalentTalent_button.setText(_translate("MainWindow", "Talent.Talent"))
        self.talent_name_button.setText(_translate("MainWindow", "Talent Name"))
        self.SpellSpellButton.setText(_translate("MainWindow", "Spell.Spell"))
        self.var_spell_name_button.setText(_translate("MainWindow", "Var:Spell Name"))
        self.class_button.setText(_translate("MainWindow", "class"))
        self.bool_button.setText(_translate("MainWindow", "bool"))
        self.private_button.setText(_translate("MainWindow", "private"))
        self.public_button.setText(_translate("MainWindow", "public"))
        self.label_input_path.setText(_translate("MainWindow", "Input Path:"))
        self.label_output_path.setText(_translate("MainWindow", "Output Path:"))
        self.InputLineEdit.setPlaceholderText(_translate("MainWindow", ""))
        self.input_browse_button.setText(_translate("MainWindow", "Browse"))
        self.output_browse_button.setText(_translate("MainWindow", "Browse"))
        self.process_button.setText(_translate("MainWindow", "Process"))

    def browse_output(self):
        # Function used to look for an output file
        file_path, _ = QFileDialog.getSaveFileName()
        if file_path:
            self.OutputLineEdit.setText(file_path)

    def insert_text(self, text):
        # Function to call associated text for button presses.
        self.InputTextBox.insertPlainText(text)

    def process_files(self):
        # Put entries of TextBox into Custom_Output File and the path from InputLineEdit to input_file_path
        custom_output = self.InputTextBox.toPlainText()
        input_file_path = self.InputLineEdit.text()
        # Opens the File on input_file_path and reads it into infile-variable
        with open(input_file_path, "r") as infile:
            content = infile.read()
            new_lines = []
            # Strip leading and trailing whitespaces
            content = content.strip()

            # checking if it's a valid idDump to remove the string and the "
            if 'idDump = "' in content:
                content = content.replace('idDump = "', '', 1).rstrip('"')

            # Formatting the content by erasing \\ and the last 2 #. After that we use ## as a delimiter
            content = content.replace('\\', '').rstrip('##')
            entries = content.split("##")
            input_file_name = os.path.basename(input_file_path).split('.')[0]

            # erasing "public static Entry and "= new Entry and checking if everything went well
            for entry in entries:
                formatted_entry = re.sub(r'public static Entry ', '', entry)
                formatted_entry = re.sub(r'= new Entry', '', formatted_entry)
                match = re.match(r'(\w+)\s*\((.+?),\s*(\d+)\);', formatted_entry)

                if not match:
                    print(f"Failed to match entry: {formatted_entry}")
                    QMessageBox.critical(None, "Error", "Invalid entry format in the input file. Please check the entries.")
                    return
                # Grouping variables
                var_spell_name, spell_name, spell_id = match.groups()
                var_talent_name, talent_name, talent_id = match.groups()

                # Checking that no empty var is getting worked with
                if input_file_name == "Spells":
                    new_line = custom_output.format(var_spell_name=var_spell_name, spell_name=spell_name, spell_id=spell_id)
                elif input_file_name == "Talents":
                    new_line = custom_output.format(var_talent_name=var_talent_name, talent_name=talent_name,
                                                    talent_id=talent_id)
                else:
                    QMessageBox.critical(None, "Error", "Invalid input file name. It should be either 'Spells' or 'Talents'.")
                    return

                new_lines.append(new_line)

            new_lines.sort()
            # Sort and format and output file.
            formatted_content = "\n".join(new_lines)
            output_file_path = self.OutputLineEdit.text()
            with open(output_file_path, "w") as outfile:
                outfile.write(formatted_content)
                QMessageBox.information(None, "Success", "File generated successfully!")
