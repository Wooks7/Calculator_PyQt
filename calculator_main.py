import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QGridLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QGridLayout()
        layout_addfeat = QGridLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("Equation: ")
        label_solution = QLabel("Solution: ")
        self.equation = QLineEdit("")
        self.solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addWidget(label_equation, 0, 0)
        layout_equation_solution.addWidget(self.equation, 0, 2)
        layout_equation_solution.addWidget(label_solution, 1, 0)
        layout_equation_solution.addWidget(self.solution, 1, 2)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_plus, 4, 0)
        layout_operation.addWidget(button_minus, 3, 0)
        layout_operation.addWidget(button_product, 2, 0)
        layout_operation.addWidget(button_division, 1, 0)

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_operation.addWidget(button_backspace, 0, 0)
        layout_operation.addWidget(button_equal, 5, 0)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        positions = [(i, j) for i in range(3, -1, -1) for j in range(3)]

        for number in range(0, 10):  # 0부터 9까지의 숫자 버튼 생성
            if number != 0:  # 숫자가 0이 아니라면
                number_button_dict[number] = QPushButton(str(number))
                number_button_dict[number].clicked.connect(lambda state, num = number:
                                                            self.number_button_clicked(num))
                x, y = positions[number - 1]
                layout_number.addWidget(number_button_dict[number], x, y)
            else:  # 숫자가 0이면
                number_button_dict[number] = QPushButton(str(number))
                layout_number.addWidget(number_button_dict[number], 4, 1)  # 0 버튼을 (3, 1) 위치에 추가

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 4, 2)

        button_double_zero = QPushButton("+/-")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 4, 0)

        ### %, CE, C, 1/x, x^2, root x 버튼 생성
        button_percentage = QPushButton("%")
        button_CE = QPushButton("CE")
        button_C = QPushButton("C")
        button_inverse = QPushButton("1/x")
        button_square = QPushButton("x^2")
        button_root = QPushButton("√")

        ### 버튼을 layout_addfeat 레이아웃에 추가
        layout_addfeat.addWidget(button_percentage, 0, 0)
        layout_addfeat.addWidget(button_CE, 0, 1)
        layout_addfeat.addWidget(button_C, 0, 2)
        layout_addfeat.addWidget(button_inverse, 1, 0)
        layout_addfeat.addWidget(button_square, 1, 1)
        layout_addfeat.addWidget(button_root, 1, 2)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution, 0, 0, 1, 0)
        main_layout.addLayout(layout_operation, 1, 1)
        main_layout.addLayout(layout_number, 1, 0)
        main_layout.addLayout(layout_addfeat, 2, 0, 1, 0)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())