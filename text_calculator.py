"""
Текстовый калькулятор

Пример:
двадцать пять плюс тринадцать -> тридцать восемь
"""

NUMBERS = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5,
           'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10,
           'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13,
           'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16,
           'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
           'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50,
           'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80,
           'девяносто': 90}

ACTIONS = ['плюс', 'минус', 'делить', 'умножить']


# def plus(a: int, b: int) -> int:
#     return a + b
#
#
# def minus(a: int, b: int) -> int:
#     return a - b
#
#
# def division(a: int, b: int) -> int:
#     return int(a / b)
#
#
# def multiply(a: int, b: int) -> int:
#     return a * b


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def calculation(text: str):
    WORDS = text.split()
    for act in ACTIONS:
        if act in WORDS:
            action = act
            index = WORDS.index(act)
            First = WORDS[:index]
            Second = WORDS[index:]

    Num_1 = 0
    Num_2 = 0

    for num in NUMBERS:
        if num in First:
            Num_1 += NUMBERS[num]

    for num in NUMBERS:
        if num in Second:
            Num_2 += NUMBERS[num]

    if action == 'плюс':
        result = Num_1 + Num_2
    elif action == 'минус':
        result = Num_1 - Num_2
    elif action == 'умножить':
        result = Num_1 * Num_2

    if (result < 11) and (result > 19) and (result > 0):
        Num_1 = get_key(NUMBERS, (result // 10) * 10)
        Num_2 = get_key(NUMBERS, result % 10) if result % 10 != 0 else ''
        result = f'{Num_1} {Num_2}'
    elif (result > -11) and (result < -19) and (result < 0):
        Num_1 = get_key(NUMBERS, (abs(result // 10)) * 10)
        Num_2 = get_key(NUMBERS, abs(result % 10)) if result % 10 != 0 else ''
        result = f'{Num_1} {Num_2}'
    else:
        result = get_key(NUMBERS, result)
    return result


print(calculation('один плюс три'))
