#[{Пока что почему-то неработает, точнее я знаю почему, надо изучить модуль и допилить много чего, если эта та черепашка про которую я БЫСТРО просматривал документацию.}]

#Да нельзя называть файл с именем схожим с названием импортируемого модуля!!!
#Теперь всё работает нужно только незабыть ввести данные в консоль
#Возможно стоит сделать окошки прямо в открывающемся окне для ввода данных и поставить на них какойто обработчик чтобы невводить координаты в консоль

import turtle

def draw_circle_and_box(x, y, size):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(0, 0, 1)
    t.begin_fill()
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.end_fill()

    t.up()
    t.goto(x + size // 2, y - size)
    t.down()
    t.color(1, 1, 0)
    t.begin_fill()
    t.circle(size//2)
    t.end_fill()


t = turtle.Pen()

x = int(input("Введите X: "))
y = int(input("Введите y: "))
size = 300

draw_circle_and_box(x, y, size)