# Игра "Аркада"
# Есть шарик, который может отскакивать от движущейся платформы. 
# Задача игрока - не дать шарику упасть ниже платформы, иначе игра окончена.

from tkinter import *
import random
import time

# создаем класс Шар
class Ball:
    # создаем конструктор шара
    def __init__(self, canvas, platform, color):
        self.canvas = canvas
        self.platform = platform
        # создаем шар с заданными параметрами
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        # создаем список с возможными скоростями
        self.speeds = [-3, -2, -1, 1, 2, 3]
        # параметр положения по оси x
        self.x = random.choice(self.speeds)
        # параметр положения по оси y
        self.y = -1
        # параметр проверки, что шарик коснулся платформы
        self.touch_bottom = False
    
    # создаем метод отрисовки шара
    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        # проверка выхода шарика за границы окна
        #---------------------------------------
        # получаем координаты шарика (метод coords возвращает 4 числа)
        pos = self.canvas.coords(self.oval)
        # x0, y0 - верхний левый угол, x1y1 - нижний правый угол
        # проверка координаты x0
        if pos[0] <= 0:
            self.x = 1
        # проверка координаты y0
        if pos[1] <= 0:
            self.y = 1
        # проверка координаты x1
        if pos[2] >= 500:
            self.x = -1
        # проверка координаты y1 (коснулись дна)
        if pos[3] >= 400:
            # self.y = -1
            self.touch_bottom = True
        # проверка, что шарик коснулся платформы
        if self.touch_platform(pos) == True:
            # направляем шарик вверх
            self.y = -1
    
    # создаем метод проверки, что шарик коснулся платформы
    def touch_platform(self, ball_pos):
        # получаем координаты платформы
        platform_pos = self.canvas.coords(self.platform.rect)
        # проверка, что шарик коснулся платформы (ось Х)
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            # проверка по оси У
            if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                return True
        return False


# создаем класс Платформа
class Platform:
    # создаем конструктор платформы
    def __init__(self, canvas, color):
        self.canvas = canvas
        # создаем платформу с заданными параметрами
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        # параметр положения по оси x
        self.x = 0
        # задаем кнопки для движения платформы
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    # создаем метод движения вправо
    def right(self, event):
        self.x = 2

    # создаем метод движения влево
    def left(self, event):
        self.x = -2
    
    # создаем метод отрисовки платформы
    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        # проверка выхода платформы за границы окна
        #---------------------------------------
        # получаем координаты платформы (метод coords возвращает 4 числа)
        pos = self.canvas.coords(self.rect)
        # проверка верхнего левого угла (x0)
        if pos[0] <= 0:
            self.x = 2    
        # проверка нижнего правого угла (x1)
        if pos[2] >= 500:
            self.x = -2    
    

window = Tk()
window.title('Аркада')
# фиксируем размеры окна по x и y
window.resizable(0, 0)
# фиксируем окно в игрой поверх всех открытых на компьютере окон
window.wm_attributes('-topmost', 1)

# создаем 'холст' для отображения объектов игры
canvas = Canvas(window, width=500, height=400)
canvas.pack()

# создаем объект платформы
platform = Platform(canvas=canvas, color='green')
# создаем объект класса Ball
ball = Ball(canvas=canvas, platform=platform, color='red')

# создаем основный цикл игры
while True:
    # проверка, что консулись дна
    if ball.touch_bottom == False:
        # отрисовываем шар
        ball.draw()
        # отрисовываем платформу
        platform.draw()
    else:
        break
    window.update()
    time.sleep(0.01)



