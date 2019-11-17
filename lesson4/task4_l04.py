"""
4. Написать скрипт, который предлагает пользователю ввести строку, 
сортирует ее элементы в прямом, 
а потом в обратном порядке и выводит на печать отсортированные строки.
"""

text = input("Enter some string.\nString: ")
lst = list(text)
asc = list(lst)
desc = list(lst)
asc.sort()
desc.sort(reverse=1)
print("ASC:", "".join(asc))
print("DESC:", "".join(desc))