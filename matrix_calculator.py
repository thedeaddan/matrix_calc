from PyQt5 import QtWidgets, QtGui
import numpy as np

class MatrixAddition(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сложение матриц')
        self.initUI()

    def initUI(self):
        self.layout = QtWidgets.QVBoxLayout()

        # Создаем виджеты для ввода размерности матриц
        self.row_label = QtWidgets.QLabel('Строки:')
        self.row_edit = QtWidgets.QLineEdit()
        self.col_label = QtWidgets.QLabel('Столбцы:')
        self.col_edit = QtWidgets.QLineEdit()

        # Создаем кнопку для запуска операции сложения матриц
        self.add_button = QtWidgets.QPushButton('Add Matrices')
        self.add_button.clicked.connect(self.add_matrices)

        # Добавляем виджеты для ввода размерности и кнопку на форму
        self.layout.addWidget(self.row_label)
        self.layout.addWidget(self.row_edit)
        self.layout.addWidget(self.col_label)
        self.layout.addWidget(self.col_edit)
        self.layout.addWidget(self.add_button)

        self.setLayout(self.layout)

        # Устанавливаем CSS стиль для формы
        self.setStyleSheet("""
            MatrixAddition {
                background-color: #f1f1f1;
                font-family: Arial;
            }
            QLabel {
                font-weight: bold;
                margin-bottom: 5px;
            }
            QLineEdit {
                padding: 5px;
                margin-bottom: 10px;
                border: none;
                border-radius: 3px;
                background-color: #fff;
                font-size: 14px;
            }
            QPushButton {
                padding: 10px;
                border: none;
                border-radius: 3px;
                background-color: #4CAF50;
                color: #fff;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3e8e41;
                cursor: pointer;
            }
            """)

    def add_matrices(self):
        # Получаем размерности матриц
        rows = int(self.row_edit.text())
        cols = int(self.col_edit.text())

        # Создаем виджеты для ввода чисел в матрицы на лету
        self.matrix1_edits = []
        self.matrix2_edits = []
        for i in range(rows):
            row_layout = QtWidgets.QHBoxLayout()
            for j in range(cols):
                edit1 = QtWidgets.QLineEdit()
                edit2 = QtWidgets.QLineEdit()
                row_layout.addWidget(edit1)
                row_layout.addWidget(edit2)
                self.matrix1_edits.append(edit1)
                self.matrix2_edits.append(edit2)
            self.layout.addLayout(row_layout)

        # Создаем кнопку для выполнения операции сложения матриц
        self.result_button = QtWidgets.QPushButton('Сложить')
        self.result_button.clicked.connect(self.calculate_result)
        self.layout.addWidget(self.result_button)

    def calculate_result(self):
        # Считываем значения из виджетов ввода чисел в матрицы
        matrix1 = np.array([float(edit.text()) for edit in self.matrix1_edits]).reshape((-1,2))
        matrix2 = np.array([float(edit.text()) for edit in self.matrix2_edits]).reshape((-1,2))

        # Выполняем операцию сложения матриц
        result = matrix1 + matrix2

        # Создаем виджет для вывода результата на экран
        result_label = QtWidgets.QLabel('Результат:')
        self.layout.addWidget(result_label)
        result_edit = QtWidgets.QTextEdit(str(result))
        result_edit.setReadOnly(True)
        self.layout.addWidget(result_edit)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MatrixAddition()
    window.show()
    app.exec_()
