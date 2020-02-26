"""
написать функцию, которая в качестве аргумента принимает строку, а возвращает список литер в верхнем регистре.
"""

text = 'hello hello'

# def upper_text(text=text):
#     char_list = list(text.upper())
#     return char_list

def upper_text(text=''):
    char_list = list(text.upper())
    return char_list

print(upper_text(text))