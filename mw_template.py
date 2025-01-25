import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # QUiLoader を使用して UI ファイルをロード
        loader = QUiLoader()
        ui_file = QFile("test_ui.ui")  # 正しいUIファイル名とパスを指定
        if not ui_file.open(QFile.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            sys.exit(-1)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        if not self.ui:
            print("Failed to load UI file.")
            sys.exit(-1)

        # UI をウィンドウ全体にセット
        self.setCentralWidget(self.ui)

        # ショートカット設定
        self.shortcut = QShortcut(QKeySequence("Ctrl+P"), self)
        self.shortcut.activated.connect(self.print_window_geometry)
        print("Debug: Shortcut Ctrl+P has been set up.")

        # UI 内のボタンを取得
        self.setup_buttons()

    def setup_buttons(self):
        """UI 内のボタン設定"""
        self.button = self.ui.findChild(QPushButton, "pushButton")
        if self.button:
            self.button.clicked.connect(self.on_button_clicked)
            print("Debug: Button found and connected.")
        else:
            print("Debug: Button not found in the UI file.")

    def on_button_clicked(self):
        """ボタンクリック時の処理"""
        print("Debug: Button clicked!")

    def print_window_geometry(self):
        """現在のウィンドウ位置とサイズを出力"""
        position = self.geometry().topLeft()  # ウィンドウの位置
        size = self.geometry().size()         # ウィンドウのサイズ
        print(f"Window Position: x={position.x()}, y={position.y()}")
        print(f"Window Size: width={size.width()}, height={size.height()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("Debug: QApplication instance created.")
    window = MyWindow()
    print("Debug: MyWindow instance created.")
    window.show()
    print("Debug: Window is now visible.")
    sys.exit(app.exec())
