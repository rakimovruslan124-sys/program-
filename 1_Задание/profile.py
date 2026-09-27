last_name = input("Ведите Фамилия: ")
first_name = input("Ведите Имя: ")
group = input("Ведите группа: ")
city = input("Ведите город: ")
age = int(input("Ведите возраст (целое число от 1 до 120): "))
favorite_subject = input("Ведите любимый предмет: ")
study_hours = float(input("Ведите количество часов подготовки в неделю: "))

age_in_four_years = age + 4
total_study_time_four_weeks = study_hours * 4
average_daily_study_time = total_study_time_four_weeks / 7

print("КАРТОЧКА СТУДЕНТА")
print(f"Имя Фамилия:  {first_name} {last_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Возраст через 4 года: {age_in_four_years}")
print(f"Время подготовки за 4 недели: {total_study_time_four_weeks:.2f} часов")
print(f"Среднее время в день: {average_daily_study_time:.2f} часов")
print(f"Любимый предмет: {favorite_subject}")