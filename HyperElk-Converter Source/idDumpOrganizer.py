import PyQt5
import PySide6
from PyQt5 import Qt


class UiDumpOrganizer(object):
    def setupUi(self, dumpOrganizer):
        dumpOrganizer.setObjectName("dumpOrganizer")
        dumpOrganizer.resize(659, 480)
        self.horizontalLayoutWidget = PyQt5.QtWidgets.QWidget(dumpOrganizer)
        self.horizontalLayoutWidget.setGeometry(PyQt5.QtCore.QRect(10, 10, 531, 461))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.listViewLayout = PyQt5.QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.listViewLayout.setContentsMargins(0, 0, 0, 0)
        self.listViewLayout.setObjectName("listViewLayout")
        self.currentSelection = PyQt5.QtWidgets.QListView(self.horizontalLayoutWidget)
        font = PyQt5.QtGui.QFont()
        font.setPointSize(12)
        self.currentSelection.setFont(font)
        self.currentSelection.setFrameShape(PyQt5.QtWidgets.QFrame.HLine)
        self.currentSelection.setAutoScroll(True)
        self.currentSelection.setEditTriggers(PyQt5.QtWidgets.QAbstractItemView.NoEditTriggers)
        self.currentSelection.setProperty("showDropIndicator", False)
        self.currentSelection.setDragEnabled(False)
        self.currentSelection.setAlternatingRowColors(False)
        self.currentSelection.setGridSize(PyQt5.QtCore.QSize(0, 0))
        self.currentSelection.setUniformItemSizes(True)
        self.currentSelection.setSelectionRectVisible(True)
        self.currentSelection.setItemAlignment(PyQt5.QtCore.Qt.AlignLeading)
        self.currentSelection.setObjectName("currentSelection")
        self.listViewLayout.addWidget(self.currentSelection)
        self.activeItems = PyQt5.QtWidgets.QListView(self.horizontalLayoutWidget)
        font = PyQt5.QtGui.QFont()
        font.setPointSize(12)
        self.activeItems.setFont(font)
        self.activeItems.setAcceptDrops(True)
        self.activeItems.setFrameShape(PyQt5.QtWidgets.QFrame.HLine)
        self.activeItems.setEditTriggers(PyQt5.QtWidgets.QAbstractItemView.NoEditTriggers)
        self.activeItems.setProperty("showDropIndicator", False)
        self.activeItems.setDragEnabled(False)
        self.activeItems.setAlternatingRowColors(False)
        self.activeItems.setUniformItemSizes(True)
        self.activeItems.setSelectionRectVisible(True)
        self.activeItems.setItemAlignment(PyQt5.QtCore.Qt.AlignLeading)
        self.activeItems.setObjectName("activeItems")
        self.listViewLayout.addWidget(self.activeItems)
        self.verticalLayoutWidget = PyQt5.QtWidgets.QWidget(dumpOrganizer)
        self.verticalLayoutWidget.setGeometry(PyQt5.QtCore.QRect(550, 360, 101, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = PyQt5.QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(PyQt5.QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_entry_button = PyQt5.QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = PyQt5.QtWidgets.QSizePolicy(PyQt5.QtWidgets.QSizePolicy.Preferred, PyQt5.QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_entry_button.sizePolicy().hasHeightForWidth())
        self.add_entry_button.setSizePolicy(sizePolicy)
        self.add_entry_button.setBaseSize(PyQt5.QtCore.QSize(0, 0))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(12)
        self.add_entry_button.setFont(font)
        self.add_entry_button.setIconSize(PyQt5.QtCore.QSize(16, 16))
        self.add_entry_button.setObjectName("add_entry_button")
        self.verticalLayout.addWidget(self.add_entry_button)
        self.select_all_button = PyQt5.QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = PyQt5.QtWidgets.QSizePolicy(PyQt5.QtWidgets.QSizePolicy.Preferred, PyQt5.QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_all_button.sizePolicy().hasHeightForWidth())
        self.select_all_button.setSizePolicy(sizePolicy)
        self.select_all_button.setBaseSize(PyQt5.QtCore.QSize(0, 0))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(12)
        self.select_all_button.setFont(font)
        self.select_all_button.setIconSize(PyQt5.QtCore.QSize(16, 16))
        self.select_all_button.setObjectName("select_all_button")
        self.verticalLayout.addWidget(self.select_all_button)
        self.delete_entry_button = PyQt5.QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = PyQt5.QtWidgets.QSizePolicy(PyQt5.QtWidgets.QSizePolicy.Preferred, PyQt5.QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_entry_button.sizePolicy().hasHeightForWidth())
        self.delete_entry_button.setSizePolicy(sizePolicy)
        self.delete_entry_button.setBaseSize(PyQt5.QtCore.QSize(0, 0))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(12)
        self.delete_entry_button.setFont(font)
        self.delete_entry_button.setIconSize(PyQt5.QtCore.QSize(16, 16))
        self.delete_entry_button.setObjectName("delete_entry_button")
        self.verticalLayout.addWidget(self.delete_entry_button)
        self.buttonBox = PyQt5.QtWidgets.QDialogButtonBox(dumpOrganizer)
        self.buttonBox.setGeometry(PyQt5.QtCore.QRect(550, 10, 101, 54))
        self.buttonBox.setOrientation(PyQt5.QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(PyQt5.QtWidgets.QDialogButtonBox.Cancel | PyQt5.QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(dumpOrganizer)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(dumpOrganizer)

    def retranslateUi(self, dumpOrganizer):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        dumpOrganizer.setWindowTitle(_translate("dumpOrganizer", "idDump Organizer"))
        self.add_entry_button.setText(_translate("dumpOrganizer", "Add Entry"))
        self.select_all_button.setText(_translate("dumpOrganizer", "Select all"))
        self.delete_entry_button.setText(_translate("dumpOrganizer", "Delete Entry"))

    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            self.process_file(file_name)

    def process_file(self, file_name):
        # Read and process the input file
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Create a model for activeItems
        model = QtGui.QStandardItemModel()

        # Add each entry to the model
        for line in lines:
            item = QtGui.QStandardItem(line.strip())
            model.appendRow(item)

        # Set the model to activeItems
        self.activeItems.setModel(model)
