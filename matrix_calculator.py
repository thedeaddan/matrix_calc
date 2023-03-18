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
        # Считываем размерности матриц
        rows = int(self.row_edit.text())
        cols = int(self.col_edit.text())

        # Создаем виджеты для ввода чисел в матрицы
        self.matrix1_edits = []
        matrix1_label = QtWidgets.QLabel('Матрица 1:')
        matrix1_layout = QtWidgets.QGridLayout()
        for row in range(rows):
            for col in range(cols):
                edit = QtWidgets.QLineEdit()
                matrix1_layout.addWidget(edit, row, col)
                self.matrix1_edits.append(edit)

        self.matrix2_edits = []
        matrix2_label = QtWidgets.QLabel('Матрица 2:')
        matrix2_layout = QtWidgets.QGridLayout()
        for row in range(rows):
            for col in range(cols):
                edit = QtWidgets.QLineEdit()
                matrix2_layout.addWidget(edit, row, col)
                self.matrix2_edits.append(edit)

        # Создаем разделительную линию между матрицами
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Создаем кнопку для расчета результата
        calculate_button = QtWidgets.QPushButton('Расчитать')
        calculate_button.clicked.connect(self.calculate_result)

        # Добавляем виджеты для ввода чисел в матрицы, разделительную линию и кнопку на форму
        self.layout.addWidget(matrix1_label)
        self.layout.addLayout(matrix1_layout)
        self.layout.addWidget(line)
        self.layout.addWidget(matrix2_label)
        self.layout.addLayout(matrix2_layout)
        self.layout.addWidget(calculate_button)


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
