# calculator v1
from colorama import Fore, Back, Style
from colorama import init
init()
print(Back.GREEN)
what = input('Что будем делать' '+, -:')
a = float(input('Первая цифра:'))
b = float(input('Вторая цифра:'))
if what == '+':
    c = a + b
    print('Результат:' + str(c))
elif what == '-':
    c = a - b
    print('Результат:' + str(c))

else:
    print('Выбрана неверная')



