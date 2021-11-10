"""
Текстовый калькулятор

Пример:
двадцать пять плюс тринадцать -> тридцать восемь
"""

NUMBERS = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4,
           'пять': 5,
           'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10,
           'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13,
           'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16,
           'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
           'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50,
           'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80,
           'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300,
           'четыресто': 400, 'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700,
           'восемьсот': 800, 'девятьсот': 900}

ACTIONS = ['плюс', 'минус', 'делить', 'умножить']


def get_key(dictionary, value):
    """
    Возвращает ключ словаря dictionary по значению value

    :param dictionary: Словарь
    :param value: Значение словаря
    :return: Возвращает ключ
    """
    for k, v in dictionary.items():
        if v == value:
            return k


def text_to_num(number) -> int:
    total = 0
    for num in NUMBERS:
        if num in number:
            total += NUMBERS[num]
    return total


def action(number_1: int, number_2: int, act: str) -> int:
    if act == 'плюс':
        return number_1 + number_2
    elif act == 'минус':
        return number_1 - number_2
    elif act == 'умножить':
        return number_1 * number_2


def num_to_text(number: int) -> str:
    """
    Переводит число в пистменный вид
    Пример: 333 -> триста тридцать три

    :param number: Переводимое число
    :return: Число в письменном виде
    """
    number = list(str(number))

    for i in range(0, len(number)):
        number[i] = int(number[i])

    if len(number) == 4:
        num_1 = get_key(NUMBERS, number[0] * 1000)
        num_2 = get_key(NUMBERS, number[1] * 100) if number[1] != 0 else ''
        num_3 = get_key(NUMBERS, number[2] * 10) if number[2] != 0 else ''
        num_4 = get_key(NUMBERS, number[3]) if number[3] != 0 else ''
        total = f"{num_1} {num_2} {num_3} {num_4} "
        return total
    elif len(number) == 3:
        num_1 = get_key(NUMBERS, number[0] * 100)
        num_2 = get_key(NUMBERS, number[1] * 10) if number[1] != 0 else ''
        num_3 = get_key(NUMBERS, number[2]) if number[2] != 0 else ''
        total = f"{num_1} {num_2} {num_3} "
        return total
    elif len(number) == 2:
        num_1 = get_key(NUMBERS, number[0] * 10)
        num_2 = get_key(NUMBERS, number[1] if number[1] != 0 else '')
        total = f"{num_1} {num_2}  "
        return total
    return get_key(NUMBERS, int(number[0]))


def calculation(text: str):
    WORDS = text.split()
    for act in ACTIONS:
        if act in WORDS:
            index = WORDS.index(act)
            First = WORDS[:index]
            Second = WORDS[index:]

            Num_1 = text_to_num(First)
            Num_2 = text_to_num(Second)

            result = action(Num_1, Num_2, act)

            return num_to_text(result)


print(calculation('пятнадцать умножить на пять'))
