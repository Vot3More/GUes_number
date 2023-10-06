import random


# Запуск игры/Starting the game
def game():
    print('Добро пожаловать в числовую угадайку')
    while True:
        print('Укажите диапазон для заданного числа\n(В пределах от 1 до 100):\n')
        x, y = is_valid_num(), is_valid_num()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y, '\n')
        compare_num(x, y)
        if continue_game():
            continue
        else:
            break


# Проверка на соответствие введенного значения числа/Checking for compliance with the entered value of the number
def is_valid(s):
    if 1 <= int(s) <= 100 and s.isdigit():
        return True
    else:
        return False


# Проверка на корректность введенного числа/Checking for the correctness of the entered number
def is_valid_num():
    while True:
        guess = input()
        if is_valid(guess):
            return int(guess)
        else:
            print('Упс, ошибочка. Введите другое число')


# Сравнение введенного числа с загаданным/Comparison of the entered number with the hidden one
def compare_num(down_num, up_num):
    number = random.randint(down_num, up_num)
    count = 0
    while True:
        user_num = is_valid_num()
        if user_num < number:
            print('Твое число меньше моего, попробуй еще раз')
            count += 1
        elif user_num > number:
            print('Нет, это большое число, введи поменьше')
            count += 1
        else:
            print('Молодец, я знал, что у тебя получится')
            print(f'Ваше количество попыток: {count}')
            break


# Предложение повторить игру/Suggestion to repeat the game
def continue_game():
    answer = input('Сыграем еще раз? (да/нет)\n')
    while True:
        if answer not in ('lf', 'yes', 'да', 'нуы', 'ytn', 'no', 'нет', 'тщ'):
            answer = input('Не, так не пойдет, ответь по человечески\nПродолжим? ("да, yes"/"нет, no")?\n')
        elif answer in ('lf', 'yes', 'да', 'нуы',):
            return True
        elif answer in ('ytn', 'no', 'нет', 'тщ'):
            print('До новый встреч!!!')
            return False


game()
