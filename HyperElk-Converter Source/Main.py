from PyQt5 import QtWidgets
from HyperElk_idDump_ConverterUI import UiMainWindow

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(main_window)

    main_window.show()
    sys.exit(app.exec_())
