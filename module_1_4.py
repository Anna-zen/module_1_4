#Практическая работа по уроку "Организация программ и методы строк."
#Цель: Написать программу на языке Python с использованием Pycharm для работы с методами строк и организации программ.
my_string = input ('Напишите мне что-нибудь: ')
print ('Вы написали: ', my_string)
print('количество символов = ', len(my_string)) # len(my_string) возвращаетчисло символов
print('Строка в верхнем регистре: ', my_string.upper()) #upper() переводит символы в верхний регистр
print('Строка в нижнем регистре:  ', my_string.lower()) # .lower() переводит символы в нижний регистр
print('Строка без пробелов:  ', my_string.replace(' ', '')) #.replace(' ', '') меняет первыйсимвол в скобках на второй
print('Первый символ:  ', my_string[0])
print('Последний символ:  ', my_string[-1])