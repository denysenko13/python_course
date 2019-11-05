from random import randint, uniform

rand_int = randint(1,100)
rand_float = uniform(1,100)

print('Integer number:', rand_int)
print('Float number:', rand_float)
print('Is int number bigger than float number?', rand_int > rand_float)