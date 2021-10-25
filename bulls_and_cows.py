# ИГРА - "Быки и Коровы"

import random

print('\nИГРА - "Быки и Коровы" \n')
print('Правила: \nВы должны отгадать 4-х значное число, которое загадал '
      'компьютер.\nЦифры в данном числе не могут повторяться.\n'
      'Бык - это цифра, которая есть в нашем загаданном числе и находится на той же позиции.\n'
      'А корова - это цифра, которая так же есть в нашем числе, но находится не на своём месте.\n'
      'Если вы получите 4 быка, то вы победили. Удачи!\n\n- - - - - - - - - -\n')


def num_uniq(number) -> bool:
    '''
    Функция определяет, есть ли в числе повторяющиеся цифры

    :param number: Проверяемое число
    :return: True если в числе нет повторяющихся цифр
    '''
    original = list(str(number))
    uniq = set(original)
    if len(original) == len(uniq):
        return True
    return False


# Компьютер загадывает число
number = 11
while num_uniq(number) == False:
    number = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + str(random.randint(0, 9))

print(f"Компьютер загадал: {number}")

UNIQ = False
<<<<<<< HEAD
COWS = 0
BULLS = 0
=======
>>>>>>> bulls_and_cows

while UNIQ == False:
    try:
        user_num = input('\nВведите число: ')
        if not num_uniq(int(user_num)):
            print('Цифры в числе не должны повторяться.')
<<<<<<< HEAD
        elif (len(str(user_num)) < 4):
=======
        elif (len(str(user_num)) != 4):
>>>>>>> bulls_and_cows
            print('Введите четырёхзначное число.')
        elif number != user_num:
            PC = list(number)
            USER = list(user_num)

<<<<<<< HEAD
            for num in USER:
                if num in PC:
                    COWS += 1
=======
            COWS = 0
            BULLS = 0

            for i in range(0, len(USER)):
                if USER[i] in PC:
                    COWS += 1
                    if i == PC.index(USER[i]):
                        BULLS += 1
            COWS = COWS - BULLS
            print(f"Коров - {COWS}")
            print(f"Быков - {BULLS}")

>>>>>>> bulls_and_cows
        else:
            UNIQ = True
    except ValueError:
        print('Вы неправильно ввели число.')

<<<<<<< HEAD
print(f'ВЫ ОТГАДАЛИ! \nКомпьютер загадал число {number}')
=======
print(f'ВЫ ОТГАДАЛИ! \nКомпьютер загадал число - {number}')
>>>>>>> bulls_and_cows
