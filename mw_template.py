import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # QUiLoader を使用して UI ファイルをロード
        loader = QUiLoader()
        ui_file = QFile("test_ui.ui")
        if not ui_file.open(QFile.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            sys.exit(-1)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        if not self.ui:
            print("Failed to load UI file.")
            sys.exit(-1)

        # ショートカット設定
        self.shortcut = QShortcut(QKeySequence("Ctrl+P"), self)
        self.shortcut.activated.connect(self.print_window_geometry)
        print("Debug: Shortcut Ctrl+P has been set up.")  # デバッグログ

    def keyPressEvent(self, event):
        """キー入力を監視してデバッグログを出力"""
        if event.type() == event.KeyPress:
            print(f"Debug: Key pressed - Key: {event.key()}, Text: {event.text()}")
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_P:
            print("Debug: Ctrl+P detected.")  # Ctrl+Pの処理
            self.print_window_geometry()
        super().keyPressEvent(event)

    def get_window_geometry(self):
        """ウィンドウの現在の位置とサイズを取得する関数"""
        position = self.geometry().topLeft()  # ウィンドウの位置 (QPoint)
        size = self.geometry().size()         # ウィンドウのサイズ (QSize)
        print("Debug: get_window_geometry called.")  # デバッグログ
        return position, size

    def print_window_geometry(self):
        """現在のウィンドウ位置とサイズを出力"""
        print("Debug: print_window_geometry activated.")  # デバッグログ
        position, size = self.get_window_geometry()
        print(f"Window Position: x={position.x()}, y={position.y()}")
        print(f"Window Size: width={size.width()}, height={size.height()}")

if __name__ == "__main__":
    print("Debug: QApplication instance is about to be created.")  # デバッグログ
    app = QApplication(sys.argv)
    print("Debug: QApplication instance created.")  # デバッグログ

    window = MyWindow()
    print("Debug: MyWindow instance created.")  # デバッグログ
    window.ui.show()  # UI を表示
    print("Debug: Window is now visible.")  # デバッグログ

    sys.exit(app.exec())
