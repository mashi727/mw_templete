import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QPoint, QSize
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # test.ui ファイルをロード
        loader = QUiLoader()
        ui_file = QFile("test_ui.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            sys.exit(-1)

        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # Command-P ショートカットを設定 (macOS 用に Meta+P に変更)
        self.shortcut = QShortcut(QKeySequence("Meta+P"), self)
        self.shortcut.activated.connect(self.print_window_geometry)

    def get_window_geometry(self):
        """ウィンドウの現在の位置とサイズを取得する関数"""
        position = self.pos()  # ウィンドウの位置 (QPoint)
        size = self.size()     # ウィンドウのサイズ (QSize)
        return position, size

    def print_window_geometry(self):
        """現在のウィンドウ位置とサイズを出力"""
        position, size = self.get_window_geometry()
        print(f"Window Position: x={position.x()}, y={position.y()}")
        print(f"Window Size: width={size.width()}, height={size.height()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.ui.show()  # UI を表示
    sys.exit(app.exec())
