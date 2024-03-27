import random
import string

# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

def generate_random_name():
    """
    Генерирует два слова из латинских букв от 1 до 15 символов
    :return:
    """
    while True:
        result = ''
        for i in range(random.randrange(1, 16)):
            result += random.choice(string.ascii_lowercase)
        result += ' '
        for i in range(random.randrange(1, 16)):
            result += random.choice(string.ascii_lowercase)
        yield result


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
