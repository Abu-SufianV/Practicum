# ИГРА - "Быки и Коровы"

import random

print('\nИГРА - "Быки и Коровы" \n')
print('Правила: \nВы должны отгадать 4-х значное число, которое загадал '
      'компьютер.\nЦифры в данном числе не могут повторяться.\n'
      'Бык - это цифра, которая есть в нашем загаданном числе и находится на той же позиции.\n'
      'А корова - это цифра, которая так же есть в нашем числе, но находится не на своём месте.\n'
      'Если вы получите 4 быка, то вы победили. Удачи!\n\n')

def num_uniq(number) -> bool:
      '''
      Функция определяет, есть ли в числе встречаюшиеся цифры

      :param number: Проверяемое число
      :return: True если в числе нет повторяющихся цифр
      '''
      original = list(str(number))
      uniq = set(original)
      if len(original) == len(uniq):
            return True
      return False
