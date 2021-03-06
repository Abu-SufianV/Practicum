""" Текстовый калькулятор """

NUMBERS = {'ноль': 0,
           'один': 1,
           'два': 2,
           'три': 3,
           'четыре': 4,
           'пять': 5,
           'шесть': 6,
           'семь': 7,
           'восемь': 8,
           'девять': 9,
           'десять': 10,
           'одиннадцать': 11,
           'двенадцать': 12,
           'тринадцать': 13,
           'четырнадцать': 14,
           'пятнадцать': 15,
           'шестнадцать': 16,
           'семнадцать': 17,
           'восемнадцать': 18,
           'девятнадцать': 19,
           'двадцать': 20,
           'тридцать': 30,
           'сорок': 40,
           'пятьдесят': 50,
           'шестьдесят': 60,
           'семьдесят': 70,
           'восемьдесят': 80,
           'девяносто': 90,
           'сто': 100,
           'двести': 200,
           'триста': 300,
           'четыресто': 400,
           'пятьсот': 500,
           'шестьсот': 600,
           'семьсот': 700,
           'восемьсот': 800,
           'девятьсот': 900,
           'одна тысяча': 1000,
           'две тысячи': 2000,
           'три тысячи': 3000,
           'четыре тысячи': 4000,
           'пять тысяч': 5000,
           'шесть тысяч': 6000,
           'семь тысяч': 7000,
           'восемь тысяч': 8000,
           'девять тысяч': 9000,
           'десять тысяч': 10000,
           'открыть скобку': '(',
           'закрыть скобку': ')'
           }

ACTIONS = ['плюс', 'минус', 'умножить', 'степени', 'делить']


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


def text_to_num(text: str) -> int:
    """
    Переводит число из письменного вида в численный

    :param text: Вводимое число
    :return: Число в численном виде
    """
    total = 0
    for num in text.split():
        if num in NUMBERS:
            total += NUMBERS[num]
    return total


def action(number_1: int, number_2: int, act: str) -> int:
    """
    Принимает два числа (int) и дейсвтие над ними в письменном виде (str)
    Например: 10, 5, "умножить" -> 50

    :param number_1: Первое число
    :param number_2: Второе число
    :param act: Действие над числами (плюс, минус, умножить)
    :return: Результат вычисления
    """
    if act == 'плюс':
        return number_1 + number_2
    elif act == 'минус':
        return number_1 - number_2
    elif act == 'умножить':
        return number_1 * number_2
    elif act == 'делить':
        return number_1 // number_2
    elif act == 'степени':
        return number_1 ** number_2


def num_to_text(number: int) -> str:
    """
    Переводит число в пистменный вид
    Пример: 333 -> триста тридцать три

    :param number: Переводимое число
    :return: Число в письменном виде
    """
    SING = True

    if number < 0:
        SING = False

    number = list(str(abs(number)))

    for i in range(0, len(number)):
        number[i] = int(number[i])

    if len(number) == 5:
        num_1 = get_key(NUMBERS, number[0] * 10000)
        total = f"{num_1}"
        return total if SING else "минус " + total
    elif len(number) == 4:
        num_1 = get_key(NUMBERS, number[0] * 1000)
        num_2 = get_key(NUMBERS, number[1] * 100) if number[1] != 0 else ''
        if (int(str(number[2]) + str(number[3])) < 11) or (
                int(str(number[2]) + str(number[3])) > 19):
            num_3 = get_key(NUMBERS, number[2] * 10) if number[2] != 0 else ''
            num_4 = get_key(NUMBERS, number[3]) if number[3] != 0 else ''
            total = f"{num_1} {num_2} {num_3} {num_4} "
        else:
            num_3 = get_key(NUMBERS, int(str(number[2]) + str(number[3])))
            total = f"{num_1} {num_2} {num_3} "
        return total if SING else "минус " + total
    elif len(number) == 3:
        num_1 = get_key(NUMBERS, number[0] * 100)
        if (int(str(number[1]) + str(number[2])) < 11) or (
                int(str(number[1]) + str(number[2])) > 19):
            num_2 = get_key(NUMBERS, number[1] * 10) if number[1] != 0 else ''
            num_3 = get_key(NUMBERS, number[2]) if number[2] != 0 else ''
            total = f"{num_1} {num_2} {num_3} "
        else:
            num_2 = get_key(NUMBERS, int(str(number[1]) + str(number[2])))
            total = f"{num_1} {num_2}"
        return total if SING else "минус " + total
    elif len(number) == 2:
        if (int(str(number[0]) + str(number[1])) < 11) or (
                int(str(number[0]) + str(number[1])) > 19):
            num_1 = get_key(NUMBERS, number[0] * 10) if number[0] != 0 else ''
            num_2 = get_key(NUMBERS, number[1]) if number[1] != 0 else ''
            total = f"{num_1} {num_2}"
        else:
            num_1 = get_key(NUMBERS, int(str(number[0]) + str(number[1])))
            total = f"{num_1}"
        return total if SING else "минус " + total
    else:
        total = get_key(NUMBERS, int(number[0]))
        return total if SING else "минус " + total


def calculation(text: str):
    """
    Данная функция производит действия над числами введённые в письменном виде.
    Например: пять умножить на три -> пятнадцать

    :param text: Вычисляемое выражение
    :return: Результат вычисления в письменном виде
    """
    WORDS = text.split()
    for act in ACTIONS:
        if act in WORDS:
            index = WORDS.index(act)
            First = WORDS[:index]
            Second = WORDS[index:]

            Num_1 = text_to_num(" ".join(First))
            Num_2 = text_to_num(" ".join(Second))

            result = action(Num_1, Num_2, act)

            return num_to_text(result)


print('\n\nДобро пожаловать в текстовый калькулятор!\n\
Вы можете проводить операции над числами в письменном виде\n\
Например: "Тридцать три умножить на одинадцать" -> "триста шестьдесят три"\n\n\
Возможные значение: от 0 до 100\n\
Возможные операции: плюс, минус, умножить, делить (нацело), в степени\n\n')

res = calculation(input("Введите выражение: "))
print(f"Ответ: {res}")
