import random
# a = random.randint(1,10)

# print(a)


print('Привет! Это игра - угадай число!')
num_1 = random.randint(1, 100)
num_2 = input(f'Введите число от 1 до 100: ')
if num_2 != num_1:
    input('Не то число, попробуйте ещё раз: ')
    
num_3 = input(f'Хотите сдаться? Yes = 1/No = 2: ')
    
if num_3 == 1:
    print('Было загадано число', num_1)
# else:
#     print('Вы - большой(ая) молодец!')

