import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # QUiLoader を使用して UI ファイルをロード
        loader = QUiLoader()
        ui_file = QFile("test_ui.ui")  # UIファイル名を指定
        if not ui_file.open(QFile.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            sys.exit(-1)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        if not self.ui:
            print("Failed to load UI file.")
            sys.exit(-1)

        # UIをウィンドウ全体にセット
        self.setCentralWidget(self.ui)

        # Quitボタンの設定
        self.setup_buttons()

    def setup_buttons(self):
        """UI 内のボタン設定"""
        self.quit_button = self.ui.findChild(QPushButton, "quitButton")
        if self.quit_button:
            self.quit_button.clicked.connect(self.close_window)
            print("Debug: Quit button found and connected.")
        else:
            print("Debug: Quit button not found in the UI file.")

    def close_window(self):
        """Quit ボタンが押されたときの動作"""
        print("Debug: Quit button clicked. Closing the window.")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
