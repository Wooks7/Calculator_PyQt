import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import re
import math

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QGridLayout()
        layout_number = QGridLayout()
        layout_addfeat = QGridLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        self.equation_solution = QLineEdit("")  # 하나의 LineEdit으로 Equation과 Solution을 표시
        self.equation_solution.setReadOnly(True)  # 읽기 전용 설정
        self.equation_solution.setAlignment(Qt.AlignRight)

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution = QGridLayout()
        layout_equation_solution.addWidget(self.equation_solution)

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
                number_button_dict[number].clicked.connect(lambda state, num = number:
                                                            self.number_button_clicked(num))
                layout_number.addWidget(number_button_dict[number], 4, 1)

        ### 소숫점 버튼과 +/- 버튼을 입력하고 시그널 설정
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

        # 버튼들의 기능 추가
        button_percentage.clicked.connect(self.button_percentage_clicked)
        button_CE.clicked.connect(self.button_CE_clicked)
        button_C.clicked.connect(self.button_C_clicked)
        button_inverse.clicked.connect(self.button_inverse_clicked)
        button_square.clicked.connect(self.button_square_clicked)
        button_root.clicked.connect(self.button_root_clicked)

        ### 버튼을 layout_addfeat 레이아웃에 추가
        layout_addfeat.addWidget(button_percentage, 0, 0)
        layout_addfeat.addWidget(button_CE, 0, 1)
        layout_addfeat.addWidget(button_C, 0, 2)
        layout_addfeat.addWidget(button_inverse, 1, 0)
        layout_addfeat.addWidget(button_square, 1, 1)
        layout_addfeat.addWidget(button_root, 1, 2)

        ## 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution, 0, 0, 1, 4)
        main_layout.addLayout(layout_operation, 1, 3, 3, 1)
        main_layout.addLayout(layout_number, 2, 0, 2, 3)
        main_layout.addLayout(layout_addfeat, 1, 0, 1, 3)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):   
        equation = self.equation_solution.text()
        if equation == '0' and num != 0 and num != '.':  # 입력된 식이 '0'이고, 입력된 숫자가 '0'이 아니며 '.'도 아닌 경우
            self.equation_solution.setText(str(num))
        elif equation == '0' and num == '.':  # 입력된 식이 '0'이고, 입력된 숫자가 '.'인 경우
            self.equation_solution.setText('0.')  # '0.'으로 식을 설정
        elif equation == '0' and num == '0':  # 입력된 식이 '0'이고, 입력된 숫자가 '0'인 경우
            pass
        else:
            equation += str(num)
            self.equation_solution.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation_solution.text()
        equation += operation
        self.equation_solution.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation_solution.text()
        solution = eval(equation)
        self.equation_solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation_solution.setText("")
        self.equation_solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation_solution.text()
        equation = equation[:-1]
        self.equation_solution.setText(equation)        

    def button_percentage_clicked(self):
        equation = self.equation_solution.text()
        if equation == '0':  # 입력된 식이 '0'인 경우
            self.equation_solution.setText('0')  # 결과를 '0'으로 설정
        else:
            try:
                result = eval(equation) / 100  # 현재 수식의 값을 100으로 나누어 백분율 계산
                self.equation_solution.setText(str(result))
            except Exception as e:
                self.equation_solution.setText("입력이 잘못되었습니다.")


    def button_CE_clicked(self):
        equation = self.equation_solution.text()
        if equation.isdigit() or equation.startswith('-'):  # 식이 숫자만으로 이루어져 있거나 음수인 경우
            self.equation_solution.setText('0')
        else:
            last_operator = max([equation.rfind(op) for op in ['+', '-', '*', '/']])
            if last_operator == -1 or last_operator == len(equation) - 1:
                self.equation_solution.setText('0')
            else:
                self.equation_solution.setText(equation[:last_operator+1])  # 연산자 이전까지의 숫자를 지움

    def button_C_clicked(self):
            self.equation_solution.setText('0')

    def button_inverse_clicked(self):
        equation = self.equation_solution.text()
        try:
            if equation:
                result = 1 / float(equation)  # 입력된 수의 역수를 계산
                self.equation_solution.setText(str(result))
            else:
                self.equation_solution.setText("0으로 나눌 수 없습니다.")
        except ZeroDivisionError:  # 입력된 수가 0인 경우
            self.equation_solution.setText("0으로 나눌 수 없습니다.")
        except Exception as e:  # 그 외의 오류가 발생한 경우
            self.equation_solution.setText("입력이 잘못되었습니다.")

    def button_square_clicked(self):
        equation = self.equation_solution.text()
        if equation:
            try:
                result = float(equation) ** 2  # 입력된 수의 제곱을 계산
                if result.is_integer():  # 계산 결과가 정수인 경우
                    result = int(result)  # 결과를 정수로 변환
                self.equation_solution.setText(str(result))
            except ValueError:
                print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")


    def button_root_clicked(self):
        equation = self.equation_solution.text()
        if equation:
            try:
                result = math.sqrt(float(equation))  # 입력된 수의 제곱근을 계산
                if result.is_integer():  # 계산 결과가 정수인 경우
                    result = int(result)  # 결과를 정수로 변환
                self.equation_solution.setText(str(result))
            except ValueError:
                print("유효하지 않은 입력입니다. 양수를 입력해주세요.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())