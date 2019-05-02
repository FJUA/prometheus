Вхідні дані: довільна, відмінна від нуля, кількість значень - аргументів командного рядка. Значеннями-аргументами можуть бути числа або рядки, які складаються з цифр та літер латинського алфавіту без пробілів.

Результат роботи: рядок, що складається з отриманих значень в зворотньому порядку, записаних через пробіл. Пробіл в кінці рядка відсутній.

Наприклад
Вхідні дані: 1
Приклад виклику: python lab4_3.py 1
Результат: 1
Вхідні дані: qwe asd zxc 123
Приклад виклику: python lab4_3.py qwe asd zxc 123
Результат: 123 zxc asd qwe
Вхідні дані: padawan young my HAVE MUST YOU PATIENCE
Приклад виклику: python lab4_3.py padawan young my HAVE MUST YOU PATIENCE
Результат: PATIENCE YOU MUST HAVE my young padawan

import sys

string = list(sys.argv[1:])
string_2 = '' 
i = 0

while i < len(string): 
	string_2 = string_2+' '+string[-1-i]
	i+=1 
string_2 = string_2.strip(); print (string_2)
