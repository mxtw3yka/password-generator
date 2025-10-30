import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit

import buttons
import password
from ui.design import Ui_MainWindow
import ui.resources
class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_slider_to_spinbox()
        self.set_password()
        self.edit_password()
        for btn in buttons.generate_password:
            getattr(self.ui,btn).clicked.connect(self.set_password)
        self.ui.btn_visibility.clicked.connect(self.change_visiblity)
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)
    def connect_slider_to_spinbox(self) -> None:
        self.ui.slider_length.valueChanged.connect(self.ui.box_length.setValue)
        self.ui.box_length.valueChanged.connect(self.ui.slider_length.setValue)
        self.ui.slider_length.valueChanged.connect(self.set_password)


    def edit_password(self) -> None:
        self.ui.line_password.textEdited.connect(self.get_entropy)
        self.ui.line_password.textEdited.connect(self.get_strength)


    def get_character(self) -> str:
        char = ''
        for btn in buttons.Characters:
            if getattr(self.ui, btn.name).isChecked():
                char += btn.value
        return char
    def set_password(self) -> None:
        try:
            self.ui.line_password.setText(
            password.create_password(length=self.ui.slider_length.value(), Characters=self.get_character())
            )
        except IndexError:
            self.ui.line_password.clear()
        self.get_entropy()
        self.get_strength()
    def get_character_number(self) -> int:
        num = 0
        for btn in buttons.character_number.items():
            if getattr(self.ui, btn[0]).isChecked():
                num += btn[1]
        return num
    def get_entropy(self) -> None:
        length = len(self.ui.line_password.text())
        char_num = self.get_character_number()
        self.ui.label_entropy.setText(
            f'Энтропия: {password.get_entropy(length, char_num)} бит'
        )

    def change_visiblity(self) -> None:
        if self.ui.btn_visibility.isChecked():
            self.ui.line_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.line_password.setEchoMode(QLineEdit.Password)
    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.line_password.text())

    def get_strength(self) -> None:
        length = len(self.ui.line_password.text())
        char_num = self.get_character_number()
        for strength in password.Strength:
            if password.get_entropy(length, char_num) >= strength.value:
                self.ui.label_strength.setText(f'Сложность: {strength.name}')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())