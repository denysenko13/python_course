"""
Просить пользователя ввести данные о себе - имя, дату рождения, профессию. 
При вводе имени, проверять, что введено имя и фамилия, через пробел. 
Если нет, кидать исключение с нужным текстом. 
При вводе даты рождения, просить вводить по отдельности - год, месяц и число. 
Если при вводе какого-то параметра введены символы, отличные от цифр, кидать исключение с нужным текстом. 
Если год больше 2000 - кидать ошибку. Если месяц больше 12, кидать ошибку. 
Если число больше 31, кидать ошибку ( ** добавить проверку, что в определенных месяцах дней может быть меньше 31). 
Сохранять данные в файл с названием {name}.txt, в формате : {name};{bith date};{profession}\n 
 
При использовании механизма исключений для проверок, лучше сначала перечислять все «неблагоприятные условия» и исключения, 
а затем код, который должен работать, в случае, если все проверки успешны, все введено корректно. 
Это сделает код более читабельным, избавит от лишних отступов и тп.
Например, функция, которая проверяет, что входная строка является числом, а число не больше 100. Сравните два варианта реализации
https://gist.github.com/kryskaks/34f83a420de15bae36c5cb49b9c27b28

Проверьте свою реализацию задания 1 из урока, если нужно, сделайте в соответствии с этой рекомендацией.
"""

COUNT_DAYS_IN_MONTH = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def collect_data():
    name = input("Enter your name: ")
    name = name.strip(" ")
    elem = name.split()
    # if not name.strip().__contains__(" "):
    #     raise Exception("Incorrect name type")
    if len(elem) != 2:
        raise Exception("Incorrect name type")
    birthday_year = input("Enter your year of birthday: ")
    # if not birthday_year.isdigit():
    #     raise Exception("Not digit")
    check_digit(birthday_year)
    if int(birthday_year) > 2000:
        raise Exception("More than 2000. Incorrect type")
    birthday_month = input("Enter your month of birthday: ")
    # if not birthday_month.isdigit():
    #     raise Exception("Not digit")
    check_digit(birthday_month)
    if int(birthday_month) > 12:
        raise Exception("More than 12. Incorrect type")
    birthday_day = input("Enter your day of birthday: ")
    # if not birthday_day.isdigit():
    #     raise Exception("Not digit")
    check_digit(birthday_day)
    if int(birthday_day) > COUNT_DAYS_IN_MONTH.get(int(birthday_month)):
        raise Exception("More than", COUNT_DAYS_IN_MONTH.get(int(birthday_month)))
    birth_date = f"{int(birthday_day):02d}.{int(birthday_month):02d}.{birthday_year}"
    profession = input("Enter your profession: ")

    return name, birth_date, profession

def check_digit(data):
    if not data.isdigit():
        raise Exception("Not digit")

def save_in_file(name, birth_date, profession):
    with open(name+".txt", 'w') as f:
        f.write(";".join([name,birth_date,profession,"\n"]))
        # f.write(f"{name};{birth_date};{profession}\n")

name, birth_date, profession = collect_data()
save_in_file(name, birth_date, profession)