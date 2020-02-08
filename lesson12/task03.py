"""
Задание по парсингу файла с погодой и получение информации о мин, макс и средней, а также дат - сделать с применением функций.
"""

WEATHER_FILE = "weather.txt"


def create_dict(file=WEATHER_FILE):
    weather_dict = dict()

    with open(file) as f:
        for line in f:
            date, value, *other = line.split(";")
            weather_dict.update({date:int(value)})
    
    return weather_dict
    
def avg_temp(weather_dict):
    value = sum(weather_dict.values()) / len(weather_dict.values())
    return round(value, 2)
    

def func_temp(weather_dict, func):
    temp = func(weather_dict.values())
    temp_dict = dict()
    for key, value in weather_dict.items():
        if value == temp:
            temp_dict.update({key:value})
    return temp_dict


# def max_temp(weather_dict):
#     max_t = max(weather_dict.values())
#     max_dict = dict()
#     for key, value in weather_dict.items():
#         if value == max_t:
#             max_dict.update({key:value})
#     return max_dict
    
# def min_temp(weather_dict):
#     min_t = min(weather_dict.values())
#     min_dict = dict()
#     for key, value in weather_dict.items():
#         if value == min_t:
#             min_dict.update({key:value})
#     return min_dict

temp = create_dict()
# print(avg_temp(create_dict()))
# print(max_temp(create_dict()))
# print(min_temp(create_dict()))

print("Average temperature in the month:",avg_temp(temp))
print("Minimum temperature:", func_temp(temp, min))
print("Maximum temperature:", func_temp(temp, max))