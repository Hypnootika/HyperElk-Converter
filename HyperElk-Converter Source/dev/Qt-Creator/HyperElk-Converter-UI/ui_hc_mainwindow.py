# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hc_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QLabel,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from browseinput import browseInput
from browseoutput import browseOutput
from converter import Converter
from edit_mirror_list import edit_mirror_list
from input_path import input_path
from output:_path import output:_path

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(900, 471)
        main_window.setMinimumSize(QSize(900, 450))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(64, 65, 66, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(96, 97, 99, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(80, 81, 82, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(32, 32, 33, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(43, 43, 44, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(33, 34, 34, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        brush8 = QBrush(QColor(186, 96, 0, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush8)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush10 = QBrush(QColor(255, 255, 255, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        brush11 = QBrush(QColor(208, 208, 208, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        brush12 = QBrush(QColor(227, 227, 227, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        brush13 = QBrush(QColor(160, 160, 160, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        brush14 = QBrush(QColor(255, 51, 51, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush14)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        brush15 = QBrush(QColor(46, 47, 48, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush16 = QBrush(QColor(105, 105, 105, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush16)
        brush17 = QBrush(QColor(29, 84, 92, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush17)
        brush18 = QBrush(QColor(240, 240, 240, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush18)
        brush19 = QBrush(QColor(53, 54, 55, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
        brush20 = QBrush(QColor(127, 127, 128, 255))
        brush20.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush17)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush18)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush19)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        main_window.setPalette(palette)
        main_window.setStyleSheet(u"font: 900 10pt \"Arial Black\";\n"
"")
        self.organizer_open = QAction(main_window)
        self.organizer_open.setObjectName(u"organizer_open")
        self.central_wgt = QWidget(main_window)
        self.central_wgt.setObjectName(u"central_wgt")
        self.gridLayoutWidget = QWidget(self.central_wgt)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 299, 711, 141))
        self.grid_buttons = QGridLayout(self.gridLayoutWidget)
        self.grid_buttons.setSpacing(4)
        self.grid_buttons.setObjectName(u"grid_buttons")
        self.grid_buttons.setContentsMargins(0, 0, 0, 0)
        self.button_talent_class = QPushButton(self.gridLayoutWidget)
        self.button_talent_class.setObjectName(u"button_talent_class")

        self.grid_buttons.addWidget(self.button_talent_class, 3, 1, 1, 1)

        self.button_talent_id = QPushButton(self.gridLayoutWidget)
        self.button_talent_id.setObjectName(u"button_talent_id")

        self.grid_buttons.addWidget(self.button_talent_id, 2, 1, 1, 1)

        self.button_talent_name_2 = QPushButton(self.gridLayoutWidget)
        self.button_talent_name_2.setObjectName(u"button_talent_name_2")

        self.grid_buttons.addWidget(self.button_talent_name_2, 1, 1, 1, 1)

        self.button_debuff_class = QPushButton(self.gridLayoutWidget)
        self.button_debuff_class.setObjectName(u"button_debuff_class")

        self.grid_buttons.addWidget(self.button_debuff_class, 1, 3, 1, 1)

        self.button_spell_name = QPushButton(self.gridLayoutWidget)
        self.button_spell_name.setObjectName(u"button_spell_name")

        self.grid_buttons.addWidget(self.button_spell_name, 1, 0, 1, 1)

        self.button_spell_id = QPushButton(self.gridLayoutWidget)
        self.button_spell_id.setObjectName(u"button_spell_id")

        self.grid_buttons.addWidget(self.button_spell_id, 2, 0, 1, 1)

        self.button_static = QPushButton(self.gridLayoutWidget)
        self.button_static.setObjectName(u"button_static")

        self.grid_buttons.addWidget(self.button_static, 3, 2, 1, 1)

        self.button_macro_class = QPushButton(self.gridLayoutWidget)
        self.button_macro_class.setObjectName(u"button_macro_class")

        self.grid_buttons.addWidget(self.button_macro_class, 3, 3, 1, 1)

        self.button_item_class = QPushButton(self.gridLayoutWidget)
        self.button_item_class.setObjectName(u"button_item_class")

        self.grid_buttons.addWidget(self.button_item_class, 2, 3, 1, 1)

        self.button_protected = QPushButton(self.gridLayoutWidget)
        self.button_protected.setObjectName(u"button_protected")

        self.grid_buttons.addWidget(self.button_protected, 2, 2, 1, 1)

        self.button_spell_class = QPushButton(self.gridLayoutWidget)
        self.button_spell_class.setObjectName(u"button_spell_class")

        self.grid_buttons.addWidget(self.button_spell_class, 3, 0, 1, 1)

        self.button_private = QPushButton(self.gridLayoutWidget)
        self.button_private.setObjectName(u"button_private")

        self.grid_buttons.addWidget(self.button_private, 1, 2, 1, 1)

        self.button_var_spell_name = QPushButton(self.gridLayoutWidget)
        self.button_var_spell_name.setObjectName(u"button_var_spell_name")

        self.grid_buttons.addWidget(self.button_var_spell_name, 0, 0, 1, 1)

        self.button_talent_name = QPushButton(self.gridLayoutWidget)
        self.button_talent_name.setObjectName(u"button_talent_name")

        self.grid_buttons.addWidget(self.button_talent_name, 0, 1, 1, 1)

        self.button_public = QPushButton(self.gridLayoutWidget)
        self.button_public.setObjectName(u"button_public")

        self.grid_buttons.addWidget(self.button_public, 0, 2, 1, 1)

        self.button_buff_class = QPushButton(self.gridLayoutWidget)
        self.button_buff_class.setObjectName(u"button_buff_class")

        self.grid_buttons.addWidget(self.button_buff_class, 0, 3, 1, 1)

        self.verticalLayoutWidget = QWidget(self.central_wgt)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(730, 79, 161, 361))
        self.vbox_list = QVBoxLayout(self.verticalLayoutWidget)
        self.vbox_list.setObjectName(u"vbox_list")
        self.vbox_list.setContentsMargins(0, 0, 0, 0)
        self.listWidget = edit_mirror_list(self.verticalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setDragDropMode(QAbstractItemView.DropOnly)
        self.listWidget.setDefaultDropAction(Qt.TargetMoveAction)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setGridSize(QSize(1, 15))
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setSortingEnabled(True)

        self.vbox_list.addWidget(self.listWidget)

        self.verticalLayoutWidget_2 = QWidget(self.central_wgt)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(729, 10, 161, 62))
        self.vbox_browse = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vbox_browse.setObjectName(u"vbox_browse")
        self.vbox_browse.setContentsMargins(0, 0, 0, 0)
        self.button_browse_input = browseInput(self.verticalLayoutWidget_2)
        self.button_browse_input.setObjectName(u"button_browse_input")

        self.vbox_browse.addWidget(self.button_browse_input)

        self.button_browse_output = browseOutput(self.verticalLayoutWidget_2)
        self.button_browse_output.setObjectName(u"button_browse_output")

        self.vbox_browse.addWidget(self.button_browse_output)

        self.verticalLayoutWidget_3 = QWidget(self.central_wgt)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(110, 10, 611, 61))
        self.vbox_path = QVBoxLayout(self.verticalLayoutWidget_3)
        self.vbox_path.setObjectName(u"vbox_path")
        self.vbox_path.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = input_path(self.verticalLayoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setProperty("IsEmpty", False)

        self.vbox_path.addWidget(self.lineEdit)

        self.lineEdit_2 = output:_path(self.verticalLayoutWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.vbox_path.addWidget(self.lineEdit_2)

        self.verticalLayoutWidget_4 = QWidget(self.central_wgt)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 10, 101, 61))
        self.vbox_label = QVBoxLayout(self.verticalLayoutWidget_4)
        self.vbox_label.setObjectName(u"vbox_label")
        self.vbox_label.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(u"label")

        self.vbox_label.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget_4)
        self.label_2.setObjectName(u"label_2")

        self.vbox_label.addWidget(self.label_2)

        self.verticalLayoutWidget_5 = QWidget(self.central_wgt)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 80, 711, 211))
        self.vbox_boxedit = QVBoxLayout(self.verticalLayoutWidget_5)
        self.vbox_boxedit.setObjectName(u"vbox_boxedit")
        self.vbox_boxedit.setContentsMargins(0, 0, 0, 0)
        self.text_edit = Converter(self.verticalLayoutWidget_5)
        self.text_edit.setObjectName(u"text_edit")
        self.text_edit.setProperty("IsValid", False)

        self.vbox_boxedit.addWidget(self.text_edit)

        main_window.setCentralWidget(self.central_wgt)
        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 900, 24))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush17)
        self.menu_bar.setPalette(palette1)
        self.menu_bar.setFocusPolicy(Qt.StrongFocus)
        self.menu_bar.setAutoFillBackground(True)
        self.menu_bar.setDefaultUp(False)
        self.menu_open = QMenu(self.menu_bar)
        self.menu_open.setObjectName(u"menu_open")
        self.menuHyperElk_Organizer = QMenu(self.menu_open)
        self.menuHyperElk_Organizer.setObjectName(u"menuHyperElk_Organizer")
        main_window.setMenuBar(self.menu_bar)

        self.menu_bar.addAction(self.menu_open.menuAction())
        self.menu_open.addAction(self.menuHyperElk_Organizer.menuAction())
        self.menuHyperElk_Organizer.addAction(self.organizer_open)

        self.retranslateUi(main_window)
        self.text_edit.textChanged.connect(self.listWidget.doItemsLayout)
        self.button_var_spell_name.clicked.connect(self.text_edit.generateOutput)
        self.button_talent_name.clicked.connect(self.text_edit.generateOutput)
        self.button_public.clicked.connect(self.text_edit.generateOutput)
        self.button_buff_class.clicked.connect(self.text_edit.generateOutput)
        self.button_spell_name.clicked.connect(self.text_edit.generateOutput)
        self.button_spell_id.clicked.connect(self.text_edit.generateOutput)
        self.button_spell_class.clicked.connect(self.text_edit.generateOutput)
        self.button_talent_name_2.clicked.connect(self.text_edit.generateOutput)
        self.button_talent_id.clicked.connect(self.text_edit.generateOutput)
        self.button_talent_class.clicked.connect(self.text_edit.generateOutput)
        self.button_private.clicked.connect(self.text_edit.generateOutput)
        self.button_protected.clicked.connect(self.text_edit.generateOutput)
        self.button_static.clicked.connect(self.text_edit.generateOutput)
        self.button_debuff_class.clicked.connect(self.text_edit.generateOutput)
        self.button_item_class.clicked.connect(self.text_edit.generateOutput)
        self.button_macro_class.clicked.connect(self.text_edit.generateOutput)
        self.button_browse_input.clicked.connect(self.lineEdit.update)
        self.button_browse_output.clicked.connect(self.lineEdit_2.constructOutputPath)
        self.button_browse_output.clicked.connect(self.lineEdit_2.update)
        self.lineEdit.editingFinished.connect(self.lineEdit_2.constructOutputPath)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.organizer_open.setText(QCoreApplication.translate("main_window", u"Open", None))
        self.button_talent_class.setText(QCoreApplication.translate("main_window", u"Talent class", None))
        self.button_talent_id.setText(QCoreApplication.translate("main_window", u"Talent ID", None))
        self.button_talent_name_2.setText(QCoreApplication.translate("main_window", u"Talent Name", None))
        self.button_debuff_class.setText(QCoreApplication.translate("main_window", u"Debuff class", None))
        self.button_spell_name.setText(QCoreApplication.translate("main_window", u"Spell Name", None))
        self.button_spell_id.setText(QCoreApplication.translate("main_window", u"Spell ID", None))
        self.button_static.setText(QCoreApplication.translate("main_window", u"static", None))
        self.button_macro_class.setText(QCoreApplication.translate("main_window", u"Macro class", None))
        self.button_item_class.setText(QCoreApplication.translate("main_window", u"Item class", None))
        self.button_protected.setText(QCoreApplication.translate("main_window", u"protected", None))
        self.button_spell_class.setText(QCoreApplication.translate("main_window", u"Spell class", None))
        self.button_private.setText(QCoreApplication.translate("main_window", u"private", None))
        self.button_var_spell_name.setText(QCoreApplication.translate("main_window", u"Variable: Spell Name", None))
        self.button_talent_name.setText(QCoreApplication.translate("main_window", u"Variable: Talent Name", None))
        self.button_public.setText(QCoreApplication.translate("main_window", u"public", None))
        self.button_buff_class.setText(QCoreApplication.translate("main_window", u"Buff class", None))
        self.button_browse_input.setText(QCoreApplication.translate("main_window", u"Browse", None))
        self.button_browse_input.setProperty("content", "")
        self.button_browse_output.setText(QCoreApplication.translate("main_window", u"Browse", None))
        self.button_browse_output.setProperty("content", "")
        self.lineEdit.setProperty("content", "")
        self.label.setText(QCoreApplication.translate("main_window", u"Input path:", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"Output path:", None))
        self.text_edit.setProperty("content_editbox", [])
        self.menu_open.setTitle(QCoreApplication.translate("main_window", u"Open", None))
        self.menuHyperElk_Organizer.setTitle(QCoreApplication.translate("main_window", u"HyperElk-Organizer", None))
    # retranslateUi

