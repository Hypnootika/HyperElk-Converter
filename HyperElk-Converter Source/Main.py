import PyQt5
from PyQt5 import QtWidgets, QtCore

from HyperElk_idDump_ConverterUI import UiMainWindow, UiDumpOrganizer

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    dump_window = QtWidgets.QWidget()
    ui = UiMainWindow()
    ui.setupUi(main_window)
    uiD = UiDumpOrganizer()
    uiD.setupUi(dump_window)

    main_window.show()
    sys.exit(app.exec_())
