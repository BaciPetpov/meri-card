from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,  
    QPushButton,QLabel)
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(Question('Гос. яз. Бразилли', 'Португальский', 'Русский','Испанский','Бразиский'))
questions_list.append(Question('Сколько времён года', '4', '3','2','1'))
questions_list.append(Question('cos 90', '0', '0,5','1','2'))

app = QApplication([])

btn_OK = QPushButton('дропнуть')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox ('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment= (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment= Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_l1 = QHBoxLayout()
layout_l2 = QHBoxLayout()
layout_l3 = QHBoxLayout()

layout_l1.addWidget(lb_Question, alignment = ( Qt.AlignHCenter | Qt.AlignVCenter) )
layout_l2.addWidget(RadioGroupBox)
layout_l2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_l3.addStretch(1)
layout_l3.addWidget(btn_OK, stretch=2)
layout_l3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_l1, stretch=2)
layout_card.addLayout(layout_l2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_l3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadoiGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следущий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_corret(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_corret('Правильно!')
        window.score += 1
        print('Статистика\nВопросов:',window.total,'\nПравельнвх ответов',window.score)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно ты бот!')
            print('Рейтинг:',(window.score/window.total*100),'%')

def next_question():
    window.total += 1
    print('Статистика\nВопросов:',window.total,'\nПравельнвх ответов',window.score)
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Record')
window.car_question = -1
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.resize(500,500)
window.show()
app.exec()