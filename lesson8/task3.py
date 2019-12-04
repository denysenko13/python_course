"""
Есть список животных, нужно определить какое животное загадал пользователь. Животные с условиями:
* Птица(bird) - может летать, есть перья
* Насекомое(insect) - может летать, нет перьев, не мышь )
* Мышь(bat) - может летать, нет перьев, мышь 
* Рыба(fish) - не может летать, живет в воде
* Млекопитающее(mammal) - не может летать, не живет в воде, есть ноги.
* Змея(snake) - не может летать, не живет в воде, нет ног.
Вопросы - через input (y, Y или n, N). Нужно узнать, что загадал пользователь.
Пример вопроса - Загаданное животное умеет летать? И так далее.
"""

bat = input("It is bat? ").lower()
if bat == 'y':
    print("This is bat")
else:
    feet = input("It have a feet? ").lower()
    if feet == 'y':
        print("This is mammal")
    else:
        water = input("It can live in water? ").lower()
        if water == 'y':
            print("This is fish")
        else: 
            fly = input("It can fly? ").lower()
            if fly == 'y':
                feathers = input("It have a feathers? ").lower()
                if feathers == 'y':
                    print("This is bird")
                else:
                    print("This is insect")
            else:
                print("This in snake")

#var 2
#fly = input("It can fly? ").lower()
#feather = input("It have feather?").lower()
#mouse = input("It is mouse?").lower()
#water = input("It can live in water?").lower()
#foot = input("It have foot?").lower()

# if fly == 'y' and feather == 'y' and mouse == 'n' and water == 'n' and foot == 'n':
#     print("This is bird")
# elif fly == 'y' and feather == 'n' and mouse == 'n' and water == 'n' and foot == 'n':
#     print("This is insect")
# elif fly == 'y' and feather == 'n' and mouse == 'y' and water == 'n' and foot == 'n':
#     print("This is bat")
# elif fly == 'n' and feather == 'n' and mouse == 'n' and water == 'y' and foot == 'n':
#     print("This is fish")
# elif fly == 'n' and feather == 'n' and mouse == 'n' and water == 'n' and foot == 'y':
#     print("This is mammal")
# elif fly == 'n' and feather == 'n' and mouse == 'n' and water == 'n' and foot == 'n':
#     print("This is snake")
# else:
#     print("This is plant")