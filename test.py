friend = 0 # Переменная, по которой мы будем определять друга в конце

name = (input('Кау тебя зовут?)\nТвоë имя: ')) # Имя участника теста
color = (input('Твой любимый цвет?\n1.Красный\n2.Синий\n3.Зелëный\nОтвет: ')) # Участник вводит любимый цвет
music = (input('Твой жанр музыки?\n1.Классика\n2.Хип-хоп\n3.Рок\nОтвет: ')) # Участник вводит любимый жанр музыки
year = (input('Твоë любимое время года?\n1.Лето\n2.Осень\n3.Весна\n4.Зима\nОтвет: ')) # Участник вводит любимое время года

if color == "Красный" or color == "красный" or color == "1." or color == 1: # Проверяем одинаковый ли у нас с ним любимый цвет
    friend += 1 # Если да, то прибавляем один к переменной friend
else:
    friend += 0 # Если нет, то значение отсаëтся исходым

if music == "Рок" or music == "рок" or music == "3." or music == 3: # Проверяем одинаковый ли у нас с ним любимый музыкальный жанр
    friend += 1
else:
    friend += 0

if year == "Зима" or year == "зима" or year == "4." or year == 4: # Проверяем одинаковый ли у нас с ним любимое время года
    friend += 1
else:
    friend += 0

if friend == 3:
    print(name, "Итог:\nМы с тобой одназначно подружимся;)")
elif friend == 2:
    print("Итог:\nНу может быть мы подружимся:/")
else:
    print('Итог:\nНу прости( Ты в пролëте чел')
