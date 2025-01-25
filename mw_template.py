import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # QUiLoaderを使用してUIファイルをロード
        loader = QUiLoader()
        ui_file = QFile("test_ui.ui")
        if not ui_file.open(QFile.ReadOnly):
            print(f"Error: Cannot open UI file: {ui_file.errorString()}")
            sys.exit(-1)
        self.loaded_ui = loader.load(ui_file)  # UIをロード
        ui_file.close()

        if not self.loaded_ui:
            print("Error: Failed to load UI file.")
            sys.exit(-1)

        print("Debug: UI file loaded successfully.")

        # ロードしたUIを中央ウィジェットとして設定
        self.setCentralWidget(self.loaded_ui)

        # ウィンドウサイズを指定
        self.resize(1280, 708)
        print(f"Debug: Window resized to 1280x708.")

        # Quitボタンを取得
        quit_button = self.loaded_ui.findChild(QPushButton, "quitButton")
        if quit_button:
            print(f"Debug: Quit button geometry: {quit_button.geometry()}")
            print(f"Debug: Quit button text: {quit_button.text()}")
            quit_button.clicked.connect(self.close)  # Quitボタンを押したらアプリを終了
        else:
            print("Error: Quit button not found in the UI.")

        # UIのすべてのボタンをデバッグ出力
        for child in self.loaded_ui.findChildren(QPushButton):
            print(f"Debug: Found button - Name: {child.objectName()}, Text: {child.text()}, Geometry: {child.geometry()}")

        # ショートカット設定
        self.shortcut = QShortcut(QKeySequence("Ctrl+P"), self)
        self.shortcut.activated.connect(self.print_window_geometry)
        print("Debug: Shortcut Ctrl+P has been set up.")

    def print_window_geometry(self):
        """現在のウィンドウ位置とサイズを出力"""
        print("Debug: print_window_geometry activated.")
        position = self.geometry().topLeft()
        size = self.geometry().size()
        print(f"Window Position: {position}, Size: {size}")


if __name__ == "__main__":
    print("Debug: QApplication instance is about to be created.")
    app = QApplication(sys.argv)
    print("Debug: QApplication instance created.")

    window = MyWindow()
    print("Debug: MyWindow instance created.")
    window.show()  # メインウィンドウを表示
    print("Debug: Window is now visible.")

    sys.exit(app.exec())
