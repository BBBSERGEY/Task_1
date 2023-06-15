# занятие 1
# numbers = [4, 8, 15, 16, 23]

# добавление элемента в конец списка
# num = int(input('Введите число, которое хотите добавить в конец списка:'))
# numbers.append(num)
# print(numbers)

# поиск суммы
# print('Начальная сумма элементов списка', sum(numbers))

# print('Минимальный элемент списка:', min(numbers))
# print('Максимальный элемент списка:', max(numbers))

# удаление элемента списка
# numbers.remove(15)
# del numbers[1]
# num = int(input('Введите число, которое удалить из списка:'))
# numbers.remove(num)
# print(numbers)

# поиск кол-ва элементов списка
# print('Длина списка:', len(numbers))

# поиск кол-ва конкретных элементов в списке
# numbers - [4, 8, 15, 16, 23, 15]
# num = int(input('Какой элемент вы хотите найти?'))
# print('В списке таких элементов:', numbers.count(num))


# упорядочить элементы в списке в порядке убывания и возрастания
# numbers = [4, 8, 8, 15, 16, 0, 23, 15, 23, 0]
# print(numbers.sort(reverse=True))
# print(numbers)
# print(numbers.sort(reverse=False))
# print(numbers)

# import random
# facts = ['Земля = третья планета от Солнца', 'Самый большой океан в мире - Тихий океан', 'В Бразилии есть кофе', 'Муравьи никогда не спят', 'Россия - самая большая по площади']

# print('Случайный факт:', random.choice(facts))

# number_of_fact = int(input('Введите номер факта, который хотите узнать:'))
# print(facts[number_of_fact - 1])

# разворот списка
# my_list = [2, 3, 1, 9, 10]
# my_list.reverse()
# print(my_list)

#изменение элемента списка по индексу
# my_list = [2, 3, 1, 9, 10]
# my list[2] = 'пять'
# print(*my_list)






# занятие 2

# import math

# import random
# my_list = [2, 1, 4, 2, 6, 9]
# # print(random.choise(my_list))
# random_element_1 = random.randint(1, 50)
# my_list.append(random_element_1)
# print(my_list)

# my_list = [2, 1, 4, 2, 6, 9]
# for i in my_list:
#     print(i)

# films = []
# num = int(input('Введите кол-во фильмов'))
# for i in range(num):
#     film = input('Введите название фильма')
#     films.append(film)
# print(*films)

# summa = 0
# # for i in range(1, 10,):
# # for i in range(1, 10, 2):
# for i in range(10, 0, -1):
#     print(i)
#     summa = summa + i
# print(summa)

# for i in range(101):
#     print(i)

# my_list = []
# for i in range(10):
#     x = random.randint(1, 10)
#     my_list.append(x)
# print(my_list)
# print(my_list.count(9))



# занятие 5
# ключ: значение

# films = {'Аватар': 2009, 'Терминатор 2': 1991, 'Оно': 2017}
# print(films)
# print(*films)
# print(films['Аватар'])

# добавление элемента в словарь (2 способа)
# 1 элемент
# films['Джунгли'] = '2019'
# print(films)
# 2 элемента
# films.update({'Оно 2': 2021, 'Война миров': 2006})
# print(films)

# удаление элемента
# del films['Аватар']
# print(films)

# проверка, есть ли ключ в словаре - if

# new_film = input('Какой фильм хотите найти?: ')
# if new_film in films:
#     print(films[new_film])
# else:
#     print('Такого фильма нет!')
#-------------------------------------------------------

# Викторина

# questions = [{'question': 'Какой океан на планете самый большой по площаде?', 
# 'answers': ['Тихий', 'Индийский'],
# 'right answer': 1}]
# questions2 = [{'question': 'Какая самая высокая гора на планете Земля?', 
# 'answers': ['Фудзи', 'Эльбрус', 'Эверест'],
# 'right answer': 3}]
# questions3 = [{'question': 'Сколько игроков в одной команде в футболе?', 
# 'answers': ['15', '11', '10', '12'],
# 'right answer': 2}]

# for quest in questions:
#     print(quest['question'])
#     answ_numb = 0
#     for answ in quest['answers']:
#         answ_numb +=1
#         print( answ_numb, answ)
#     user_answ = int(input('Введите номер ответа: '))
#     if user_answ == quest['right answer']:
#         print('Верно!')
#     else:
#         print('Неправильно!')
#     print('---------------------------------------------')    

# for quest in questions2:
#     print(quest['question'])
#     answ_numb = 0
#     for answ in quest['answers']:
#         answ_numb +=1
#         print( answ_numb, answ)
#     user_answ = int(input('Введите номер ответа: '))
#     if user_answ == quest['right answer']:
#         print('Верно!')
#     else:
#         print('Неправильно!')
#     print('---------------------------------------------')  

# for quest in questions3:
#     print(quest['question'])
#     answ_numb = 0
#     for answ in quest['answers']:
#         answ_numb +=1
#         print( answ_numb, answ)
#     user_answ = int(input('Введите номер ответа: '))
#     if user_answ == quest['right answer']:
#         print('Верно!')
#     else:
#         print('Неправильно!')
#     print('---------------------------------------------')  

# if 'right answer' == 3:
#     print('Выйграл!')





# n = int(input('Введите N:'))

# def summa_n(n):
#     if n==0:
#         return n
#     else:
#         return(n+summa_n(n-1))
# print(f'Сумма чисел от 1 до {n} = {summa_n(n)}')

# или минималистичный вариант:

# print(f'Сумма чисел от 1 до N = {sum(range(int(input("Введите N:"))+1))}')

# def greating():
#     print('Привет!')
# print('Добро пожаловать!')
# for i in range(5):
#     a = input('Зайдёте? Да/Нет: ')
# if a == 'Да':
#     print('Привет!\n')
#     print('Добро пожаловать!')
# print('Следующий.\n')


# from tkinter import *

# def on_click():
#     if int(count_time['text']) > 0:
#         count_time['text'] = int(count_time['text']) - 1
#         count_time.place(x=250, y=400)
#         window.after(1000, on_click)
#     else:
#         width_new = window.winfo_screenwidth()
#         height_new = window.winfo_screenheight() 
#         window.geometry(str(width_new) + 'x' + str(height_new))
#         photo = PhotoImage(file='skelet.jpg')
#         photo_label = Label(image=photo, bg='black')
#         photo_label.image = photo
#         photo_label.place(width=width_new, height=height_new, x=0, y=0)

# window = Tk()
# window.geometry('800x600')
# window.title('Something dangerous')
# window.config(bg='black')
# window.resizable(width=False, height=False)
# text = Label(text='Ваш компьютер заражён!', fg='red', font=('Times New Roman', 34), bg='black')
# text.place(x=50, y=200)
# window.protocol('WM_DELETE_WINDOW')
# count_time = Label(text='7', fg='green', font=('Times New Roman', 34), bg='black')


# window.mainloop()


# занятие 10

# num = int(input('Введите число:'))
# cur_num = 1
# while cur_num <= num:
#     print(cur_num)
#     cur_num +=1


# import random

# films = ['Форсаж','Терминатор', 'Оно 2', 'Аватар', 'Джон Уик', 'Мстители', 'Властелин колец', 'Интерстеллар', 'Человек-паук', 'Матрица', 'Конан-варвар']

# print('Привет! Сейчас я буду показывать тебе случайный фильм')
# while True:
#     print(random.choice(films))
#     answer = input('Нужно еще? Y/N: ')
#     while answer != 'Y' and answer != 'N':
#         answer = input('Пожалуйста, введите ответ в формате Y/N:')
#     if answer == 'N':
#         break    

# print('Приятного просмотра!')

# -----------------------------------------------------------------

# генерация PDF-файлов
# from fpdf import FPDF
# pdf_file = FPDF('P', 'cm', (10, 15))

# # страница
# pdf_file.add_page()

# pdf_file.set_font('arial', size=16)
# pdf_file.set_text_color(120, 35, 90)
# pdf_file.set_fill_color(0, 0, 120)

# # цвет рисования
# pdf_file.set_draw_color(0, 255, 0)

# pdf_file.cell(8, 5, txt='Welcome!', align='C', border=1, fill=True)

# # добавляем картинку
# pdf_file.image('pic.jpg', h=0, w=10, x=0, y=5)


# pdf_file.output('my_pdf.pdf')




#-----------------------------------------------------------------------
# урок 11
# from fpdf import FPDF

# from datetime import datetime

# pdf = FPDF('P', 'mm', 'A4')
# pdf.add_page()

# pdf.image('bg.jpg', h=297, w=210, x=0, y=0)

# pdf.add_font('comic', '', 'C:\Windows\Fonts\comic.ttf', uni=True)
# pdf.set_font('comic', size=37)
# pdf.set_text_color(0, 0, 0)

# name = input('Кому предназначается открытка?')

# # линия сверху
# pdf.cell(0, 95, ln=1)
# pdf.cell(0, 20, txt='Дорогой '+ name + '!', align='C', ln=1)

# pdf.set_font('comic', size=18)
# text = input('Введите текст поздравления:')
# pdf.set_right_margin(50)
# pdf.set_left_margin(50)
# pdf.multi_cell(0, 20, txt=text, align='C')

# today = datetime.today().strftime('%d.%m.%y')
# pdf.set_text_color(124, 89, 147)
# pdf.cell(0, 10, txt=today, align='R', ln=1)

# author_name = input('Введите своё имя:')
# pdf.cell(0, 10, txt=author_name, align='R', ln=1)


# pdf.output('holiday.pdf')


# ------------------------------------------------

# from tkinter import *

# def draw_menu():
#     # clear()
#     menu_title = Label(text='Что бы вы хотели сделать?', font=('Arial', 24), fg='white', bg='orange')
#     menu_title.place(width=700, height=50, x=0, y=0)
#     b_1 = Button(text='Узнать что-то новое', font=('Arial', 18), fg='black', command=clear)
#     b_1.place(x=25, y=75, width=300)

#     b_2 = Button(text='Посмотреть на котиков', font=('Arial', 18), fg='black', command=clear)
#     b_2.place(x=375, y=75, width=300)

# def clear():
#     all_widgets = window.place_slaves()
#     for wid in all_widgets:
#         wid.destroy()
#     draw_home_button()

# def draw_home_button():
#     b_home = Button(text='Домой', font=('Arial', 24), fg='black', command=draw_menu)
#     b_home.place(x=25, y=500, width=150)

# window = Tk()
# window.geometry('700x600')

# draw_menu()

# window.mainloop()





# МОДУЛЬ 2 ==============================================================


# урок 3

# from tkinter import *
# class House:
#     def __init__(self, roof_color, wall_color, height, width):
#         self.roof_color = roof_color
#         self.wall_color = wall_color
#         self.height = 140
#         self.width = 130

#     def build_house(self, x, y):
#         h = self.height
#         w = self.width

#         self.wall = canvas.create_rectangle(x + 20, y, x + 120, y + 100, fill=self.wall_color)
#         self.roof = canvas.create_polygon(x, y, x + w, y, x + w/2, h - 100, fill=self.roof_color)



# window = Tk()
# window.geometry('800x600')

# canvas = Canvas(window ,width=800, height=600, bg='white')
# canvas.create_rectangle(10, 10, 110, 110, fill='red', outline='')
# canvas.create_rectangle(10, 150, 190, 250, fill='blue', outline='')
# canvas.pack()

# house_1 = House('green', 'black')
# house_1.build_house(20, 50)
# house_2 = House('red', 'blue')
# house_2.build_house(180, 50)

# window.mainloop()



# # class House:
# #     def __int__(self, roof_color, wall_color, height, width):






# -----------------------------------------------------------------------
# урок 4

# from tkinter import *
# import random
# window = Tk()

# w = 600
# h = 600
# window.geometry(f'{w}x{h}')

# # холст для отрисовки игрового поля
# canvas = Canvas(window, width=w, height=h)
# canvas.place(in_=window, x=0, y=0)
# # задний фон
# bg_photo = PhotoImage(file='bg_2.png')

# # класс Рыцарь
# class Knight:
#     def __init__(self):
#         # атрибуты рыцаря
#         self.x = 70
#         self.y = h // 2
#         # скорость рыцаря
#         self.v = 0
#         # изображение рыцаря
#         self.photo = PhotoImage(file='knight.png')


#     def up(self, event):
#         self.v = -3

#     def down(self, event):
#         self.v = 3    

#     def stop(self, event):
#         self.v = 0   

# class Dragon:
#     def __init__(self):
#         self.x = 750
#         self.y = random.randint(100, 500) 
#         self.v = random.randint(2, 3)    
#         self.photo = PhotoImage(file='dragon.png')

# # создаем анимацию игры
# def game():
#     canvas.delete('all')
#     # задний фон отображаем
#     canvas.create_image(300, 300, image=bg_photo)
#     # рыцаря отображаем
#     canvas.create_image(knight.x, knight.y, image=knight.photo)
#     # меняем положение рыцаря
#     knight.y += knight.v

#     # счетчик текущего дракона
#     current_dragon = 0
#     # индекс дракона, которго delete с canvas 
#     dragon_to_delete = -1

#     for dragon in dragons:
#         # перемещаем дракона к рыцарю
#         dragon.x -= dragon.v
#         # отображаем дракона левее
#         canvas.create_image(dragon.x, dragon.y, image=dragon.photo)

#         if ((knight.x - dragon.x)**2 + (knight.y - dragon.y)**2) <= 96**2:
#             dragon_to_delete = current_dragon
#         current_dragon +=1
#         if dragon.x <=0:
#             canvas.delete('all')
#             canvas.create_text(w // 2, h // 2, text='You lose!', font='Verdana 40', fill='red')
#             break
#     if dragon_to_delete > -1:
#         del dragons[dragon_to_delete]


#     if len(dragons) == 0:
#         canvas.delete('all')
#         canvas.create_text(w // 2, h // 2, text='You win!', font='Verdana 40', fill='green')
#     else:
#         window.after(10, game)



# knight = Knight()
        

# # создаем список с драконами
# dragons = []
# for i in range(random.randint(2, 5)):
#     dragons.append(Dragon())

# # закрепляем кнопки за вызовом функций движения рыцаря
# window.bind('<Key-Up>', knight.up)
# window.bind('<Key-Down>', knight.down)
# window.bind('<KeyRelease>', knight.stop)

# # запускаем игру
# game()
# window.mainloop()



# ---------------------------------------------------------------------
# урок 1

# num_1 = float(input('Введите 1 число'))
# num_2 = float(input('Введите 2 число'))
# print(num_1 + num_2)
# % - деление с остатком
# // - целочисленное деление
# import math

# def cool_calculator():
#     num_1 = float(input('Введите 1 число'))
#     num_2 = float(input('Введите 2 число'))
#     oper = input('Введите операцию')
#     operations = ['+', '-', '*', '/', 'D']
#     while oper not in operations:
#     # while oper != '+' and oper != '-' and oper != '*' and oper != '/':
#         oper = input('Такой операции нет! Введи: * / + - D')
#     if oper == '+':
#         # print('Сумма чисел', num_1, 'и', num_2, 'равна', num_1 + num_2)
#         print(f'Сумма чисел {num_1} и {num_2} равна {num_1 + num_2}')
#     elif oper == '-':
#         print(f'Разность чисел {num_1} и {num_2} равна {num_1 - num_2}')
#     elif oper == '*':
#         print(f'Произведение чисел {num_1} и {num_2} равна {num_1 * num_2}')
#     elif oper == '/':
#         if num_2 == 0:
#             print('На 0 делить нельзя!')
#         else:        
#             print(f'Частное от деления чисел {num_1} и {num_2} равна {num_1 / num_2}')
#     if oper == 'D':
#         print("Введите коэффициенты для уравнения")
#         print("ax^2 + bx + c = 0:")
#         a = float(input("a = "))
#         b = float(input("b = "))
#         c = float(input("c = "))    
#         discr = b ** 2 - 4 * a * c
#         print("Дискриминант D = %.2f" % discr)  

#     else:
#         print('Такой операции нет! Введи: * / + - D')
    
# count = int(input('Введите кол-во вычислений:'))
# for i in range(1, count + 1):
#     print(f'Вычисление № {i}.')
#     cool_calculator()
#     print('--------------------------------------------------------------------------------------')
# print('Вычисления окончены!')






#------------------------------------------------------------------
# урок 5

# import requests

# # def check_people(link):
# #     for i in range(1, 6):
# #         data = requests.get(f'{link}/{i}').json()
# #         print(data['name'], data['mass'])

# # def check_starships(link):
# #     for i in range(1, 6):
# #         try:
# #             data = requests.get(f'{link}/{i}').json()
# #             print(data['name'])
# #         except KeyError:
# #             print('Данные не найдены')

# def check_planets(link):
#     diameter_list = [1, 2, 4]
#     for i in range(1, 6):
#         data = requests.get(f'{link}/{i}').json()
#         print(data['name'], data['diameter'])
#         diameter_list.append([data['name'], data['diameter']])
#     return diameter_list


# url = 'https://swapi.dev/api/'

# response = requests.get(url).json()

# # people_api = response.get('people')
# # # check_people(people_api)
# # starships_api = response.get('starships')
# planets_api = response.get('planets')
# max_diameter = max(diameter_list)
# # print(check_planets(planets_api))
# print(max_diameter)

# ------------------------------------------------------------------------------------
# урок 2

# import telebot
# token = '5988479219:AAFu0d9zradUdQcIjsLm3bOUXsJtJ9G1vTw'
# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start', 'help']) 
# def send_welcome(message):
#     welcome_text = 'Привет! Я умею отправлять интересный факт, а также отправлять картиночки. А еще могу отправлять музыку и котиков!'
#     # создаем клавиатуру
#     keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
#     button1 = telebot.types.KeyboardButton('Факт')
#     button2 = telebot.types.KeyboardButton('Стишок')
#     button3 = telebot.types.KeyboardButton('Котики')
#     button4 = telebot.types.KeyboardButton('Стикеры')
#     button5 = telebot.types.KeyboardButton('Песенка')
#     keyboard.add(button1, button2, button3, button4, button5)
#     bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)





# # последняя строчка в коде, чтобы бот работал постоянно(пока работает программа)
# bot.polling()





# урок 6 ------------------------------------------------------------------

# from bs4 import BeautifulSoup as bs
# import requests
# from datetime import datetime
# def get_data(id):
#     return xml.find('Valute', {'ID': 'R01010'}).Value.text
# url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
# # сегодняшняя дата
# today = datetime.today()
# # вытаскиваем дату
# today = today.strftime("%d/%m/%Y")

# # запрос к API Центробанка
# response = requests.get(url + f'date_req={today}')

# # получаем XML файл 
# xml = bs(response.content, features="xml")
# print(get_data("R01235"), "рублей за 1 доллар")
# print(get_data("R01239"), "рублей за 1 евро")
# # print(xml.find('Valute', {'ID': 'R01010'}).Value.text)
# # data = xml.find_all('Name')
# # for name in data:
# #     print(name.text)


# урок 9 -------------------------------------------------------------------------------


# import random

# def create_file():
#     letters = [chr(i) for i in range(ord('a'), ord('z'), + 1)]
#     for _ in range(10000):
#         num = random.randint(1, 10000)
#         file.write(str(num) + '\n')

# file = open('data.txt')

# my_list = [int(i) for i in file if int(i) % 2 == 0]

# print(len(my_list))

# file.close()


# урок 7 ------------------------------------------------

# прога 1
# текст в голос

# from gtts import gTTS

# file = open('data1.txt', encoding='utf-8')
# data_text = file.read()
# tts = gTTS(text=data_text, lang='ru')
# tts.save('converted_file.mp3')


# прога 2
# import pyaudio
# import speech_recognition as sr

# rec = sr.Recognizer()

# while True:
#     with sr.Microphone(device_index=1) as source:
#         print('Скажи что-нибудь...')
#         audio = rec.listen(source)
#     speech = rec.recognize_google(audio, language='ru_RU').lower()
#     print('Вы сказали:', speech)
#     if speech == 'привет':
#         print('Здравствуйте!')
#     elif speech == 'стоп':
#         print('До свидания!')        
#         break



# урок 8 ------------------------------------------------------------------------------------

# from tkinter import *
# from PIL import Image, ImageTk
# import requests
# from bs4 import BeautifulSoup as bs
# from datetime import datetime

# def get_data(id):
#     return xml.find('Valute', {'ID': id}).Value.text


# window = Tk()
# window.geometry('800x500')
# window.title('Курс валют')

# url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
# today = datetime.today()
# today = today.strftime('%d/%m/%Y')
# payload = {'date_req': today}
# response = requests.get(url, params=payload)
# xml = bs(response.content, features='xml')

# # img_logo = PhotoImage(file='japan.png')

# # logo = Label(window, image=img_logo)
# # logo.place(x=0, y=0)

# name_prog = Label(window, text='Курс валют \n Cool-банк', fg='black', font='Arial 22')
# name_prog.place(x=110, y=25)

# date = Label(window, text='Курс на: ' + today.replace('/', '.'), fg='black', font='Arial 18')
# date.place(x=100, y=150)

# # данные о долларе
# usd = Label(window, text='Доллар США: $' + get_data('R01235'), font='Arial 16')
# usd.place(x=100, y=190)

# # данные о евро
# eur = Label(window, text='Евро: €' + get_data('R01239'), font='Arial 16')
# eur.place(x=100, y=230)

# # данные о фунте
# lb = Label(window, text='Фунт стерлингов Соединенного королевства: £' + get_data('R01035'), font='Arial 16')
# lb.place(x=100, y=270)

# # данные о австр долларе
# lb = Label(window, text='Австралийский доллар: $' + get_data('R01010'), font='Arial 16')
# lb.place(x=100, y=310)

# # данные о гривне
# lb = Label(window, text='Украинских гривен: ₴' + get_data('R01720'), font='Arial 16')
# lb.place(x=100, y=350)

# # данные о юане
# lb = Label(window, text='Китайский юань: ¥' + get_data('R01375'), font='Arial 16')
# lb.place(x=100, y=390)

# window.mainloop()



# урок 10 ---------------------------------------------------------------------

# class Human:
#     name = 'Иван'
#     color_of_hair = 'blue'
#     height = '180'
#     age = 28
#     weight = 70

# human_1 = Human()
# human_2 = Human()
# print(human_1.name)
# print(human_2.color_of_hair)

# class Human:
#     def __init__(self, name, color_of_hair, height, weight, age):
#         self.name = name
#         self.color_of_hair = color_of_hair
#         self.height = height
#         self.weight = weight
#         self.age = age

# human_1 = Human('Петя', 'red', 180, 70, 28)
# # print(human_1.__dict__)
# human_1.name = 'Александр'
# # print(human_1.__dict__)

# # my_name = input('Введите свое имя: ')
# human_2 = Human(name='Арсений', color_of_hair='green', age=25, height=178, weight=72)
# # print(human_1.name, human_2.name)
# # print('Разница в возрасте =', abs(human_1.age - human_2.age))
# humans = []
# humans.append(human_1)
# humans.append(human_2)
# print(humans)

# class Tank:
#     def __init__(self, model, armor, damage, health):
#         self.model = model
#         self.armor = armor
#         self.damage = damage
#         self.health = health

#     def print_info(self):
#         print(f"{self.model} имеет лобовую броню {self.armor}, {self.health} ед. здоровья и урон {self.damage} ед.")

#     def get_damage(self, enemy_damage):
#         self.health -= enemy_damage
#         if self.health > 0:
#             print(f'{self.model}:')
#             print(f'Командир, по нашему танку попали, у нас осталось {self.health} очков здоровья!')
#         else:
#             print(f'{self.model}:')
#             print('Командир, наш танк подбит!')

#     def deal_damage(self, enemy):
#         if enemy.health > 0 and self.health > 0:
#             enemy.get_damage(self.damage)
#             print(f'{self.model}:')
#             print(f'Есть пробитие! У противника {enemy.model} осталось {enemy.health} очков здоровья')
#         elif enemy.health <= 0 and self.health > 0:
#             print(f'{self.model}:')
#             print(f'Экипаж танка {enemy.model} уже уничтожен!')
#         elif self.health <= 0:
#             print(f'{self.model}:')
#             print(f'Мы уже подбиты, стрельба невозможна')

# class Super_Tank(Tank):
#     def __init__(self, model, armor, damage, health):
#         super().__init__(model, armor, damage, health)

#     def get_damage(self, enemy_damage):
#         super().get_damage(enemy_damage / 2)

# tank_1 = Tank(model='T-34', armor=45, damage=110, health=450)
# tank_2 = Tank(model='M4-Sherman', armor=48, damage=105, health=480)
# tank_3 = Tank(model='PzkpfW-4', armor=50, damage=150, health=430)

# tank_1.print_info()
# tank_2.print_info()
# tank_3.print_info()

# tank_1.deal_damage(tank_2)
# tank_2.deal_damage(tank_1)
# tank_3.deal_damage(tank_1)
# tank_1.deal_damage(tank_3)
# tank_2.deal_damage(tank_3)
# tank_3.deal_damage(tank_2)
# tank_1.deal_damage(tank_2)
# tank_2.deal_damage(tank_1)
# tank_3.deal_damage(tank_1)
# tank_1.deal_damage(tank_3)
# tank_2.deal_damage(tank_3)
# tank_3.deal_damage(tank_2)
# tank_1.deal_damage(tank_2)
# tank_2.deal_damage(tank_1)
# tank_3.deal_damage(tank_1)
# tank_1.deal_damage(tank_3)
# tank_2.deal_damage(tank_3)
# tank_3.deal_damage(tank_2)




# урок 11 ----------------------------------------------------------------------------------------------------------

# num_1 = 123
# num_2 = 'hello'
# print(type(num_1))

# для чиел от -5 до 256 id() не меняется
# num_1 = 5
# num_2 = 5
# list_1 = [1, 2, 3]
# list_2 = [1, 2, 3]
# print(id(list_1), id(list_2))

# Инкапсуляция
# class Example:
#     def public_method(self):
#         return 42
#     def _private_method(self):
#         return 'test'
#     def __protected_method(self):
#         return 'Hello!'
# obj = Example()
# print(obj.public_method())
# print(obj._private_method())
# # print(obj.__protected_method())
# print(obj._Example__protected_method())

# шаблон проектирования Singleton('Одиночка')
# Зачем нужен этот шаблон? Для того, чтобы создать ОДИН объект класса и предоставить к нему глобальную точку доступа
# class Singleton(object):
#     def __new__(cls):
#         if hasattr(cls, 'instance') == False:
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance

# obj_1 = Singleton()
# print('Объект создан:', obj_1, id(obj_1))
# obj_2 = Singleton()
# print('Объект создан:', obj_2, id(obj_2))



# урок 12 ==========================================================================================================

# Игра "Аркада"
# Есть шарик, который может отскакивать от движущейся платформы. 
# Задача игрока - не дать шарику упасть ниже платформы, иначе игра окончена.

# from tkinter import *
# import random
# import time

# # создаем класс Шар
# class Ball:
#     # создаем конструктор шара
#     def __init__(self, canvas, platform, color):
#         self.canvas = canvas
#         self.platform = platform
#         # создаем шар с заданными параметрами
#         self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
#         # создаем список с возможными скоростями
#         self.speeds = [-3, -2, -1, 1, 2, 3]
#         # параметр положения по оси x
#         self.x = random.choice(self.speeds)
#         # параметр положения по оси y
#         self.y = -1
#         # параметр проверки, что шарик коснулся платформы
#         self.touch_bottom = False
    
#     # создаем метод отрисовки шара
#     def draw(self):
#         self.canvas.move(self.oval, self.x, self.y)
#         # проверка выхода шарика за границы окна
#         #---------------------------------------
#         # получаем координаты шарика (метод coords возвращает 4 числа)
#         pos = self.canvas.coords(self.oval)
#         # x0, y0 - верхний левый угол, x1y1 - нижний правый угол
#         # проверка координаты x0
#         if pos[0] <= 0:
#             self.x = 1
#         # проверка координаты y0
#         if pos[1] <= 0:
#             self.y = 1
#         # проверка координаты x1
#         if pos[2] >= 500:
#             self.x = -1
#         # проверка координаты y1 (коснулись дна)
#         if pos[3] >= 400:
#             # self.y = -1
#             self.touch_bottom = True
#         # проверка, что шарик коснулся платформы
#         if self.touch_platform(pos) == True:
#             # направляем шарик вверх
#             self.y = -1
    
#     # создаем метод проверки, что шарик коснулся платформы
#     def touch_platform(self, ball_pos):
#         # получаем координаты платформы
#         platform_pos = self.canvas.coords(self.platform.rect)
#         # проверка, что шарик коснулся платформы (ось Х)
#         if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
#             # проверка по оси У
#             if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
#                 return True
#         return False


# # создаем класс Платформа
# class Platform:
#     # создаем конструктор платформы
#     def __init__(self, canvas, color):
#         self.canvas = canvas
#         # создаем платформу с заданными параметрами
#         self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
#         # параметр положения по оси x
#         self.x = 0
#         # задаем кнопки для движения платформы
#         self.canvas.bind_all('<KeyPress-Left>', self.left)
#         self.canvas.bind_all('<KeyPress-Right>', self.right)

#     # создаем метод движения вправо
#     def right(self, event):
#         self.x = 2

#     # создаем метод движения влево
#     def left(self, event):
#         self.x = -2
    
#     # создаем метод отрисовки платформы
#     def draw(self):
#         self.canvas.move(self.rect, self.x, 0)
#         # проверка выхода платформы за границы окна
#         #---------------------------------------
#         # получаем координаты платформы (метод coords возвращает 4 числа)
#         pos = self.canvas.coords(self.rect)
#         # проверка верхнего левого угла (x0)
#         if pos[0] <= 0:
#             self.x = 2    
#         # проверка нижнего правого угла (x1)
#         if pos[2] >= 500:
#             self.x = -2    
    

# window = Tk()
# window.title('Аркада')
# # фиксируем размеры окна по x и y
# window.resizable(0, 0)
# # фиксируем окно в игрой поверх всех открытых на компьютере окон
# window.wm_attributes('-topmost', 1)

# # создаем 'холст' для отображения объектов игры
# canvas = Canvas(window, width=500, height=400)
# canvas.pack()

# # создаем объект платформы
# platform = Platform(canvas=canvas, color='green')
# # создаем объект класса Ball
# ball = Ball(canvas=canvas, platform=platform, color='red')

# # создаем основный цикл игры
# while True:
#     # проверка, что консулись дна
#     if ball.touch_bottom == False:
#         # отрисовываем шар
#         ball.draw()
#         # отрисовываем платформу
#         platform.draw()
#     else:
#         break
#     window.update()
#     time.sleep(0.01)





# модуль 3 ========================================================================================================================

# ---------------------------------------------------------------------------------------------------------------------------------



# урок 1 ============================================

# name = 'Игорь'
# salary = 200_000

# print(f'Имя работника: {name}, З/П в месяц: {salary}')
# print(f'З/П в год: {salary * 12}')

# employee = {
#     'name': 'Игорь',
#     'salary': 200_000
# }

# employees = [
#     {
#         'name': 'Игорь',
#         'salary': 200_000
#     },

#     {
#         'name': 'Дима',
#         'salary': 300_000
#     },

#     {
#         'name': 'Вася',
#         'salary': 150_000
#     },
# ]

# for employee in employees:
#     if employee['name'] == 'Игорь':
#         employees.remove(employee)
#         break

# new_employee = {
#     'name': 'Кирилл',
#     'salary': 200_000
# }
# employees.append(new_employee)
# print(f'Текущее кол-во сотрудников: {len(employees)}')

# print(employees[1])

# в виде Класса

# class Employee:
#     def __init__(self, name, salary, on_vacation, is_good_employee):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = on_vacation
#         self.is_good_employee = is_good_employee
#     def get_info(self):
#         return f'У сотрудника по имени {self.name} З/П в месяц: {self.salary}. В отпуске? - {self.on_vacation}. Хороший сотрудник? - {self.is_good_employee}'

# employees = [Employee('Игорь', 200_000, 'В отпуске', 'True'), Employee('Никита', 250_000, 'Не в отпуске', 'True'), Employee('Роман', 300_000, 'Не в отпуске', 'True'), Employee('Сергей', 280_000, 'Не в отпуске', 'True'), Employee('Иван', 310_000, 'Не в отпуске', 'False')]

# new_name = input('Введите имя сотрудника:')
# new_salary = int(input('Введите З/П:'))
# new_on_vacation = input('Введите, в отпуске ли сотрудник:')
# is_good_employee = input('Введите, хороший ли сотрудник(True/False):')
# employees.append(Employee(new_name, new_salary, new_on_vacation, is_good_employee))
# # del ('Иван', 310_000, 'Не в отпуске', 'False')
# for employee in employees:
#     if employee['is_good_employee'] == 'False':
#         employees.remove('Иван', 310_000, 'Не в отпуске', 'False')
#         break

# for employee in employees:
#     print(employee.get_info())



# урок 2 -------------------------------------------------------------

# бот ВК
# import vk_api
# import requests

# token = 'vk1.a.t5jyQiuYFDJbgqVgnbSSdcwnsa4Fd-68ez4I3a6xb4B6ctOcQui82NeIjVwuqi6w_4gbCJ-IgQCZiLjfJbVgMP_v7kM3YnmCnR_fmCXqDK4oQkZ75jfnPPtLcUMCLklQbcH6lVj9opdrxa7zOQfrQSOjMrSgasa8p5OrLty0KZNz6nTvUF5J_YUiUX0HCELsGRi_Um9__5axtHvsh7s7kA'

# # управление ботом
# vk = vk_api.VkApi(token=token)

# vk._auth_token()

# # messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})

# # print(messages['items'][0]['last_message']['from_id'])
# # print(messages['items'][0]['last_message']['text'])
# # print(messages['items'][0]['last_message']['id'])

# while True:
#     messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
#     if messages['count'] > 0:
#         user_id = messages['items'][0]['last_message']['from_id']
#         text = messages['items'][0]['last_message']['text']
#         text_id = messages['items'][0]['last_message']['id']
#         # бот отвечает 
#         vk.method('messages.send', {'peer_id': user_id, 'random_id': text_id, 'message': 'Ваше сообщение получено!'})
#         if text.lower() == 'привет':
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': text_id, 'message': 'Добрый день!'})
#         elif text.lower() == 'планеты':
#             url = 'https://swapi.dev/api'
#             response = requests.get(url).json()

#             planets_api = response.get("planets")
#             def check_planets(url):
#                 max_diam = 0
#                 planets_list = []
#                 for i in range(1, 11):
#                     response = requests.get(f'{url}/{i}').json()
#                     planets_list.append({response.get('name'): response.get('diameter')})
#                     diam = float(response.get('diameter'))
#                     if diam > max_diam:
#                         max_diam = diam

#                 # print(planets_list)
#                 # print('\n', max_diam)
#             check_planets(planets_api)
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': text_id, 'message': 'Наибольший диаметр:'})
#         elif text.lower() == 'корабли':
#             url = 'https://swapi.dev/api'
#             response = requests.get(url).json()

#             ships_api = response.get("starships")
#             def check_planets(url):
#                 max_speed = 0
#                 ships_list = []
#                 for i in range(1, 11):
#                     response = requests.get(f'{url}/{i}').json()
#                     ships_list.append({response.get('name'): response.get('max_atmosphering_speed')})
#                     speed = float(response.get('max_atmosphering_speed'))
#                     if speed > max_speed:
#                         max_speed = speed
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': text_id, 'message': 'Наибольшая скорость:'})
#         else:
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': text_id, 'message': 'Простите, я вас не понимаю...'})




# урок 3 -----------------------------------------------------------

# import vk_api
# from vk_api.longpoll import VkLongPoll, VkEventType
# from bot1 import get_course
# import random

# vk_token = 'vk1.a.t5jyQiuYFDJbgqVgnbSSdcwnsa4Fd-68ez4I3a6xb4B6ctOcQui82NeIjVwuqi6w_4gbCJ-IgQCZiLjfJbVgMP_v7kM3YnmCnR_fmCXqDK4oQkZ75jfnPPtLcUMCLklQbcH6lVj9opdrxa7zOQfrQSOjMrSgasa8p5OrLty0KZNz6nTvUF5J_YUiUX0HCELsGRi_Um9__5axtHvsh7s7kA'

# vk_session = vk_api.VkApi(token=vk_token)

# vk = vk_session.get_api()
# longpoll = VkLongPoll(vk_session)

# hello_message = 'Привет! Я бот, который может выполнять следующие команды: \n \
#                 -k курс валют'

# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#         msg = event.text.lower()
#         user_id = event.user_id
#         random_id = random.randint(1, 10_000)

#         # обрабатываем сообщение, где есть 'привет'
#         if 'привет' in msg:
#             vk.messages.send(user_id=user_id, random_id=random_id, message=hello_message)

#         elif msg == '-k':
#             response = f"{get_course('R01235')} рублей за 1 доллар \n  \
#             {get_course('R01239')} рублей за 1 евро \n  \
#             {get_course('R01375')} рублей за 10 юаней \n  \
#             {get_course('R01035')} рублей за 1 фунт \n"
#             vk.messages.send(user_id=user_id, random_id=random_id, message=response)

#         else:
#             vk.messages.send(user_id=user_id, random_id=random_id, message='Простите, я вас не понимаю!')




# урок 4 =================================================================================================================
# Создайте функцию – контекст менеджер, которая будет получать на вход ID валюты и возвращать информацию о ней в виде:

# (1 шт.) Австралийский доллар стоит(ят) 49,2779 руб.

# Если такой валюты нет – ошибка должна обрабатываться и выводиться, что такая валюта не найдена.











# import time
# строгие вычисления
# num_list = [i for i in range(1000000)]

# ленивые вычисления
# num_list = (i for i in range(100))
# for i in num_list:
#     print(i)

# time_list = [time.sleep(i) for i in range(1, 4)]
# print(time_list)

# time_list = (time.sleep(i) for i in range(1, 4))
# print(time_list)

# num_list = (i**3 for i in range(100))

# new_list = list(num_list)
# print(new_list)

# ключевое слово yield
# def my_func():
#     for i in range(10):
#         yield i

# for x in my_func():
#     print(x)


# def my_func():
#     for i in range(1 ,11):
#         print(f"До {i}")
#         yield i
#         print(f"После {i}")
# for i in my_func():
#     print(i)


# with open('test.txt', 'w') as f:
#     f.write('Hello, world!')
#     print(f.closed)
# print(f.closed)

# создаем менеджер контекста
# import contextlib

# @contextlib.contextmanager
# def str_reverse(my_str):
#     print('Входим в контекстный менеджер:')
#     yield my_str[::-1]
#     print('Выходим из контекстного менеджера')

# with str_reverse('Hello, world!') as reversed_str:
#     print(f'Выполняется код: {reversed_str}')


# def some_func(*args, **kwargs):
#     print(args, kwargs)
#     print(type(args))
#     print(type(kwargs))

# some_func(1, 2, a=3, b=5, c=6)




# урок 5 ================================================================================================

# import random
# import time

# class TimeWork:
#     def __init__(self):
#         self.start = None

#     def __enter__(self):
#         self.start = time.time()
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         end = time.time()
#         time_work = end - self.start
#         print(f'Время работы программы: {time_work} сек.')
#         # глушим вызываемое исключение TypeError
#         # if exc_type is TypeError:
#         # глушим любые исключения
#         if exc_type is not None:
#             return True


# with TimeWork() as t1:
#     num_list = [i for i in range(1_000_000)]
#     num_list -= 'kek'
#     print(1 / 0)

# exc_type - тип исключения
# exc_val - значение исключения
# exc_tb - объект трассировки


# num_list = [1, 2, 3, 4]
# list_iter = iter(num_list)
# print(next(list_iter))

# for i in list_iter:
#     print(i)

# class RandomIter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.reload = limit

#     def __iter__(self):
#         self.limit = self.reload
#         return self

#     def __next__(self):
#         if self.limit == 0:
#             raise StopIteration
#         self.limit -= 1
#         return random.randint(1, 100)

# rand_iter = RandomIter(5)

# for rand_int in rand_iter:
#     print(rand_int)
# print('---------------------------------------')
# for rand_int in rand_iter:
#     print(rand_int)



# урок 6 =============================================================================

# сеттеры и геттеры

# class Year:
#     def __init__(self, days, season):
#         self.__days = days
#         self.__season = season

# # создаем геттер для получения кол-ва дней
#     def get_days(self):
#         return self.__days
    
#     def get_season(self):
#         return self.__season
    
# # создаем сеттеры

#     def set_days(self, new_days):
#         if 365 <= new_days <= 366:
#             self.__days = new_days
#         else:
#             raise Exception('Некорректное значение')

#     def set_season(self, new_season):
#         self.__season = new_season

# class Human:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name

#     @name.deleter
#     def name(self):
#         self.__name = None

#     @age.setter
#     def age(self, new_age):
#         if new_age <= 0:
#             raise ValueError('Отрицательное значение возраста')
#         self.__age = new_age  

#     @age.deleter
#     def age(self):
#         self.__age = None           



# person = Human('Александр', 28)
# print(person.name)
# print(person.age)
# person.name = 'Василий'
# person.age = 32
# print(person.name)
# print(person.age)


# my_year = Year(366, 'Winter')
# my_year.set_days(365)
# print(my_year.get_days())

# my_year.set_season('Summer')
# print(my_year.get_season())


# Перепишите наш первый класс года со свойством property, как во втором примере из урока.

# class Year:
#     def __init__(self, days, season):
#         self.__days = days
#         self.__season = season

#     @property
#     def days(self):
#         return self.__days
            
#     @property
#     def season(self):
#         return self.__season
    
#     @days.setter
#     def days(self, new_days):
#         if 365 <= new_days <= 366:
#             self.__days = new_days
#         else:
#             raise Exception('Некорректное значение')

#     @days.setter
#     def season(self, new_season):
#         self.__season = new_season





# урок 7 =================================================================================================

# метод __add__

# # класс для описания товара
# class Item:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight

#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
        
#         elif isinstance(other, int) or isinstance(other, float):
#            return self.price + other
        
#     def __sub__(self, other):
#         if isinstance(other, Item):
#             return self.price - other.price
        
#         elif isinstance(other, int) or isinstance(other, float):
#            return self.price - other


#     def __mul__(self, other):
#         if isinstance(other, Item):
#             return self.weight * other.weight

#         elif isinstance(other, int) or isinstance(other, float):
#             return self.weight * other

#     def __truediv__(self, other):
#         if isinstance(other, Item):
#             return self.weight / other.weight

#         elif isinstance(other, int) or isinstance(other, float):
#             return self.weight / other

# item_1 = Item('Видеокарта', 37_500, 1.4)
# item_2 = Item('Процессор', 19_000, 0.2)

# total_price = item_1 + item_2
# sub_price = item_1 - item_2
# mul_weight = item_1 * item_2
# truediv_weight = item_1 / item_2
# print('Сумма товаров =', total_price)
# print('Разница цен товаров =', sub_price)
# print('Произведение веса товаров =', mul_weight)
# print('Частное веса товаров =', truediv_weight)

# __sub__()
# __mul__()
# __truediv__()

# Игра Алхимия

# from tkinter import *
# from random import randint

# window = Tk()
# window.geometry('600x600')

# class Fire:
#     image = PhotoImage(file='fire.png').subsample(8, 8)

#     def __add__(self, other):
#         if isinstance(other, Earth):
#             return Clay

# class Water:
#     image = PhotoImage(file='water.png').subsample(8, 8)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Steam

# class Wind:
#     image = PhotoImage(file='wind.png').subsample(8, 8)

# class Earth:
#     image = PhotoImage(file='earth.png').subsample(8, 8)

#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Clay

# class Clay:
#     image = PhotoImage(file='clay.png').subsample(8, 8)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Brick

# class Steam:
#     image = PhotoImage(file='steam.png')

# class Brick:
#     image = PhotoImage(file='brick.png')

# def move(event):
#     images_id = canvas.find_overlapping(event.x, event.y, event.x + 5, event.y + 5)
#     canvas.coords(images_id, event.x, event.y)

#     # соединение элементов
#     if len(images_id) == 2:
#         elem_id_1 = images_id[0]
#         elem_id_2 = images_id[1]
#         element_1 = elements[elem_id_1 - 1]
#         element_2 = elements[elem_id_2 - 1]

#         new_element = element_1 + element_2
#         if new_element:
#             if new_element not in elements:
#                 canvas.create_image(event.x, event.y, image=new_element.image)
#                 elements.append(new_element)

#     if len(images_id) == 2:
#         elem_id_3 = images_id[0]
#         elem_id_4 = images_id[1]
#         element_3 = elements[elem_id_3 - 1]
#         element_4 = elements[elem_id_4 - 1]

#         new_element = element_3 + element_4
#         if new_element:
#             if new_element not in elements:
#                 canvas.create_image(event.x, event.y, image=new_element.image)
#                 elements.append(new_element)

#     if len(images_id) == 2:
#         elem_id_5 = images_id[0]
#         elem_id_6 = images_id[1]
#         element_5 = elements[elem_id_5 - 1]
#         element_6 = elements[elem_id_6 - 1]

#         new_element = element_5 + element_6
#         if new_element:
#             if new_element not in elements:
#                 canvas.create_image(event.x, event.y, image=new_element.image)
#                 elements.append(new_element)                

# canvas = Canvas(window, width=600, height=600)
# canvas.pack()

# elements = [Earth(), Water(), Wind(), Fire()]

# for elem in elements:
#     canvas.create_image(randint(50, 550), randint(50, 550), image=elem.image)

# # связываем лкм с меремещением картинки
# window.bind('<B1 Motion>', move)

# window.mainloop()




# урок 8 ===================================================================================

# 1. Лямбда-функция

# data = [1, 4, 5, 2, 6]
# print(sorted(data))


# def is_odd(n):
#     return n % 2 != 0

# def is_even(n):
#     return n % 2 == 0


# a = ['wewds', 'dfdf', 'ds', 'q']
# print(sorted(a, key=len, reverse=True))


# data = [2, 3, 1, 6, 6, 3, 7, 8, 6]
# print(sorted(data, key=lambda n: n % 2 != 0))

# def phone_price(phone):
#     return phone['price']

# from pprint import pprint

# phones = [
#     {
#         'name': 'IPhone 14',
#         'brand': 'Apple',
#         'price': 1200
#     },
#     {
#         'name': 'Samsung Galaxy A53',
#         'brand': 'Samsung',
#         'price': 500
#     },
#     {
#         'name': 'Google Pixel 7',
#         'brand': 'Google',
#         'price': 650
#     },
#     {
#         'name': 'Iphone 13',
#         'brand': 'Apple',
#         'price': 1000
#     },
# ]

# pprint(sorted(phones, key=lambda phone: phone['price']))


# 2. Функция filter()
# data = [2, 3, 1, 6, 6, 3, 7, 8, 6]
# print(list(filter(lambda n: n % 2 == 0, data)))

# apple_list = list(filter(lambda phone: phone['brand'] == 'Apple', phones))
# pprint(apple_list)


# 3. Функция map()
# num1, num2, num3 = map(int, input().split())
# print(num1, num2, num3)
# data = list(map(int, input().split()))
# print(data)

# names = ['Иван', 'Петя', 'Костя']
# surnames = ['Петров', 'Иванов', 'Сидоров']
# full_names = list(map(lambda name, surname: f'{name} {surname}', names, surnames))
# print(full_names)


# 4. Функция enumerate()
# data = [3, 5, 7, 2, 1, 4, 9, 6, 8, 10]
# print(list(enumerate(data)))

# indexed_phones = []
# for index, phone in enumerate(phones):
#     indexed_phones.append({index: phone})

# pprint(indexed_phones)


# 5. Функция zip()
# names = ['Иван', 'Петя', 'Костя']
# surnames = ['Петров', 'Иванов', 'Сидоров']
# patronymics = ['Дмитриевич', 'Егорович', 'Павлович']
# for name, surname, patronymic in zip(names, surnames, patronymics):
#     print(name, surname, patronymic)






# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand

#     def __repr__(self):
#         return self.brand

# items = [
#     {
#         'price': '1000',
#         'brand': 'Apple'
#     },
#     {
#         'price': '1200',
#         'brand': 'Apple'
#     },   
#     {
#         'price': '900',
#         'brand': 'Samsung'
#     },
#     {
#         'price': '700',
#         'brand': 'Samsung'
#     },
#     {
#         'price': '660',
#         'brand': 'Xiaomi'
#     },
# ]
  
# result = list(filter(lambda brand: brand['brand'] == 'Apple', items))
# print(result)


# names_list = ['данил', 'артём', 'никита', 'влад']
# type(names_list)
# print(names_list)
# # print(sorted(names_list, key=lambda names: names[names_list.capitalize()]))

# pprint(sorted(phones, key=lambda phone: phone['price']))
# print(string.capitalize(names_list))


# print(sorted(names_list, key=lambda names_list: str(names_list.capitalize())))


# names_list = ['данил', 'артём', 'никита', 'влад']
# result = [name.capitalize() for name in names_list]
# print(result)




# -------------------------------------------------------------------------------------------------------------------------
# урок 11
# import sqlite3
# from pprint import pprint

# class User:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
        
# def create_table_users(cursor):
#     command = """
#     CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     surname TEXT,
#     gender TEXT);
#     """

#     cursor.execute(command)

# def add_user(cursor, user):
#     command = """
#     INSERT INTO users (name, surname, gender)
#     VALUES (?, ?, ?);
#     """

#     cursor.execute(command, (user.name, user.surname, user.gender))

# def get_users_list(cursor):
#     command = """
#     SELECT * FROM users;
#     """
#     result = cursor.execute(command)
#     users_list = result.fetchall()
#     pprint(users_list)

# def delete_one_user(cursor):
#     command = """
#     DELETE FROM users
#     WHERE id = 2;
#     """
#     cursor.execute(command)

# def delete_users(cursor):
#     command = """
#     DELETE FROM users;
#     """
#     cursor.execute(command)

# def get_user(cursor, user_id):
#     command = """
#     SELECT * FROM users
#     WHERE id = ?;
#     """
#     result = cursor.execute(command, (user_id,))

#     user = result.fetchall()
#     print(user)

# def update_user_name(cursor, user_id, new_value):
#     command = """
#     UPDATE users
#     SET name = ?
#     WHERE id = ?;
#     """
#     cursor.execute(command, (new_value, user_id))

# def delete_user_id(cursor):
#     command = """
#     DELETE FROM users
#     WHERE Id=2;
#     """
#     cursor.execute(command)


# with sqlite3.connect('data.db') as cursor:

#     create_table_users(cursor)

#     delete_users(cursor)

#     add_user(cursor, User(name='Вася', surname='Иванов', gender='male'))
#     add_user(cursor, User(name='Иван', surname='Васильев', gender='male'))
#     add_user(cursor, User(name='Лиза', surname='Петрова', gender='female'))


#     get_users_list(cursor)
#     delete_user_id(cursor)

# Добавьте функцию, которая выводит список сотрудников по их полу (все мальчики или все девочки).

    # delete_one_user(cursor)
    # update_user_name(cursor)
    # get_user(cursor)

    # update_user_name(cursor, 2, 'Михаил')
    # get_user(cursor, 2)

# CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     surname TEXT,
#     gender TEXT);

# Продолжите расширять функционал работы с базой данных. Добавьте функцию, которая удаляет не всю информацию из таблицы, а лишь конкретного пользователя по его id.



# ----------------------------------------------------------------------------------------------------------------------------------------

# урок 12

# import os
# import pathlib

# def get_all_files(my_path):
#     for name in os.listdir(my_path):
#         new_path = os.path.join(my_path, name)
#         if os.path.isdir(new_path):
#             print('Папка:', name)
#             get_all_files(new_path)
#         else:
#             print('-', name)

# current_path = os.path.abspath(__file__)

# parent_path = os.path.join(current_path, '..')
# parent_path = pathlib.Path(current_path).parent

# get_all_files(parent_path)
# # print(parent_path)


# n = int(input())
# factorial = 1
# for i in range(1, n + 1):
#     factorial = factorial * i
# print(factorial)


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(4))




# -----------------------------------------------------------------------------------------------------------------

# МОДУЛЬ 4



# урок 1 ----------------------------------------------------------------------------------------------------------

import time

def count_sym(line):
    for sym in set(line):
        counter = 0
        for sub_sym in line:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)

start =time.time()

count_sym('asbasbsa' * 100000)

end = time.time()

result = end - start
print(result)




















































































































































































































































































































































































































































































































































































