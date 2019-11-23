"""
3. Создать файл с именем persons.txt и записать в него строки из задания 1 - про Росса и Гарри. 
Добавьте символ перехода на новую строку \n в конце каждой строки при добавлении в файл.
"""

l = "harry potter; 30; 127.45 galeon; auror,\nross geller; 34; 6500.45 usd; paleontologist"

with open('./persons.txt', 'a') as f:
    f.write(l)

