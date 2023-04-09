#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import shuffle
app = QApplication([])

class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

question_list = []
question_list.append(Question('Скоко людей живут на земле', '7,837 миллиарда', '1 мильон', '1 человек', '15 человек'))
question_list.append(Question('Скоко людей живут в россий', '143,4 миллиона' , '123' , '1 тысяча' , '45 людей'))
question_list.append(Question('Скоко людей живут в китае', '1,412 миллиарда', '1200 миллиард', '333 людей' , '9 людей'))

shuffle(question_list)

main_win = QWidget()
main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')
btn_OK = QPushButton('Ответить')
RadionGroupBox = QGroupBox("Варианты ответов")
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Смурфы')
btn_answer3 = QRadioButton('Чулымцы')
btn_answer4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()

RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

H1 = QHBoxLayout()
H2 = QVBoxLayout()
H3 = QVBoxLayout()

H2.addWidget(btn_answer1)
H2.addWidget(btn_answer2)
H3.addWidget(btn_answer3)
H3.addWidget(btn_answer4) 

H1.addLayout(H2)
H1.addLayout(H3)

RadionGroupBox.setLayout(H1)

AnswerGroup = QGroupBox('Результат теста')
Lb_resual = QLabel('правельный/неправельный')
Lb_current = QLabel('Правельный ответ')
answer_line = QVBoxLayout()

AnswerGroup.setLayout(answer_line)

answer_line.addWidget(Lb_resual)
answer_line.addWidget(Lb_current)


main_line = QVBoxLayout()
main_line.addWidget(question)
main_line.addWidget(RadionGroupBox)
main_line.addWidget(AnswerGroup)
main_line.addWidget(btn_OK)
AnswerGroup.hide()

def show_result():
    RadionGroupBox.hide()
    AnswerGroup.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    AnswerGroup.hide()
    RadionGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def start():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    question.setText(q.question)
    Lb_current.setText(q.right_answer)
    show_question()

def next_question():
    main_win.num_of_question +=1
    if main_win.num_of_question == len(question_list):
        main_win.num_of_question = 0
    q = question_list[main_win.num_of_question]
    ask(q)

def check_answer():
    if answers[0].isChecked() == True:
        Lb_resual.setText('Правильно!')
    else:
        Lb_resual.setText('Неверно!')
    show_result()

main_win.num_of_question = -1
next_question()
btn_OK.clicked.connect(start)
main_win.setLayout(main_line)
main_win.show()
app.exec()