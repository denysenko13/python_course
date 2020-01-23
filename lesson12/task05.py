"""
5. Осуществлять подсчёт количества букв в тексте, текст брать из файла или просить пользователя вводить. 
На выходе - словарь. Ключ - буква лат алфавита, значение - количество, сколько раз она встречалась в тексте. 
Брать только буквы, приводить в нижний регистр, все остальные символы - игнорировать, в т ч пробелы. 
** Подготовить информацию чуть более усложнённо, ключ - буква, значение - список слов, где она встречается.
"""
import string

WHITESPACES_LiST = list(string.whitespace)
PUNCTUATIONS_LIST = list(string.punctuation)
LETTERS_LIST = list(string.ascii_lowercase)
TEXT_FILE = "python_zen.txt"
data_source = ""
source_type = input("For file enter \"file\", fore custom text enter \"custom\": ")
words = list()


def file_type(data_source):
    words = list()

    with open(data_source) as f:
        for line in f:
            words += (line.split(" "))
    strips = WHITESPACES_LiST + PUNCTUATIONS_LIST
    for i in strips:
        words = [word.strip(i) for word in words]
    words = [word for word in words if word != ""]
    words.sort(key=len)

    return words


def custom_type(data_source):
    words = list()
    words += (data_source.split(" "))
    strips = WHITESPACES_LiST + PUNCTUATIONS_LIST
    for i in strips:
        words = [word.strip(i) for word in words]
    words = [word for word in words if word != ""]
    words.sort(key=len)

    return words    


def create_letters_list(words):
    letters_list = list()
    for word in words:
        for letter in list(word):
            if letter.isalpha():
                letters_list.append(letter.lower())
    letters_list.sort()
    
    return letters_list


def letters_count(letters_list):
    letters_dict = dict()
    for letter in LETTERS_LIST:
        letters_dict.update({letter : letters_list.count(letter)})

    return letters_dict


def letters_in_words(letters_list, words):
    ltrs_in_wrds = dict(zip(LETTERS_LIST, [[]]*len(LETTERS_LIST)))
    for letter in LETTERS_LIST:
        for word in words:
            if letter in word.lower():
                lst_words = list(ltrs_in_wrds.get(letter))
                lst_words.append(word)
                ltrs_in_wrds[letter] = lst_words

    return ltrs_in_wrds


if source_type == "custom":
    data_source = input("Enter some text: ")
    words = custom_type(data_source)
elif source_type == "file":
    data_source = TEXT_FILE
    words = file_type(data_source)
else:
    print("Unknown type")

print(letters_count(create_letters_list(words)))
print(letters_in_words(create_letters_list(words), words))
# for k, v in letters_in_words(create_letters_list(words), words).items():
#     print(k, v)