"""
2. Осуществить парсинг файла с информацией о температуре воздуха. 
Вывести дату(хотя бы одну) минимальной температуры и само значение температуры, дату максимальной температуры и значение. 
Вывести среднее значение температуры за месяц. 
* Если минимальная или максимальная температура была не один день, то вывести все даты, когда была зафиксирована такая температура.
"""

weather_file = "weather.txt"
weater_dict = dict()

with open(weather_file) as file:
    for line in file:
        date, value, *other = line.split(";")
        # weater_dict.update({date:int(value)})
        weater_dict[date] = int(value)


max_temp = max(weater_dict.values())
min_temp = min(weater_dict.values())
avg_temp = sum(weater_dict.values())/len(weater_dict.values())

for key, value in weater_dict.items():
    if value == min_temp:
        print("Minimum temperature:", key, value)
    if value == max_temp:
        print("Maximum temperature:", key, value)
print("Average temperature in the month:", round(avg_temp, 2))

# max_t = -1000
# min_t = 1000
# avg = 0

# for value in weater_dict.values():
#     avg += value
#     if value > max_t:
#         max_t = value
#     if value < min_t:
#         min_t = value

# for key, value in weater_dict.items():
#     if value == min_t:
#         print("Minimum temperature:", key, value)
#     if value == max_t:
#         print("Maximum temperature:", key, value)
# print("Average temperature in the month:", round(avg/len(weater_dict), 2))
