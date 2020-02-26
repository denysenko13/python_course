def parse_line(text):
    text = text.strip()
    splitted = text.split(';')
    if len(splitted) != 2:
        raise ValueError("Invalid line format")

    return splitted[0], int(splitted[1])


def parse_file(file_name='weather.txt'):
    stat = {}
    with open(file_name) as f:
        for line in f:
            date, temp = parse_line(line)
            stat[temp] = date

        print(stat)
        return stat


def find_extremum(stat, func):
    return func(stat.keys())


statistics = parse_file()
min_temp = find_extremum(statistics, min)
print(f'min_temp = {min_temp} on date: {statistics.get(min_temp)}')