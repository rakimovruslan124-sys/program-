# названия аудиторий
first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

# исходные значения
print("Исходные значения:")
print("Первая аудитория:", first_room)
print("Вторая аудитория:", second_room)

temp = first_room 
first_room = second_room 
second_room = temp  

# результат
print("После обмена:")
print("Первая аудитория:", first_room)
print("Вторая аудитория:", second_room)
