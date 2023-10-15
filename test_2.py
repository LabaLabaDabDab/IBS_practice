def find_in_different_registers(words):
    unique_words = set()

    for word in words:
        unique_words.add(word.lower())

    result = sorted(list(unique_words))

    return result


words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
print(find_in_different_registers(words))

"""
# На вход подаётся массив слов зависимых от регистра, для которых необходимо произвести фильтрацию на основании дублей слов,
# если в списке найден дубль по регистру, то все подобные слова вне зависимости от регистра исключаются.
# На выходе должны получить уникальный список слов в нижнем регистре.
 
words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
# find_in_different_registers(words) -> ['папа', 'брат']
 
 
def find_in_different_registers(words):
  pass
 
print(find_in_different_registers(words))
"""
