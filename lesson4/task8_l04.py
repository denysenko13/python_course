"""
8. Написать скрипт, который просит пользователя ввести следующую информацию:
имя и фамилию работника (один input), его должность, зарплату, возраст.
Вывести на печать анкету работника в формате:
Имя: <имя>, Фамилия: <фамилия>, возраст: <возраст>. Должность: <должность>. Зарплата: <зарплата>
При выводе имени и фамилии удостоверьтесь, что они будут выведены с Большой Буквы независимо от того,
как были введены пользователем, также не забудьте очистить от лишних пробелов. 
При выводе зарплаты, иметь в виду, что интересующая нас точность - до копеек. 
Использовать два варианта форматирования строк, на ваш выбор. 
"""

info = input("Enter your first and last name, position, salary, age\n")
first_name, last_name, position, salary, age = info.split()
print("First name: {first_name}, Last name: {last_name}, age: {age}. Position: {position}. Salary: {salary:.2f}".format(first_name=first_name.capitalize(),last_name=last_name.capitalize(),age=int(age),position=position,salary=float(salary)))
print(f"First name: {first_name.capitalize()}, Last name: {last_name.capitalize()}, age: {int(age)}. Position: {position}. Salary: {float(salary):.2f}")