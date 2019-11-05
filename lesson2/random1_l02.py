from random import randint, uniform

x = randint(1,100)
y = uniform(1,100)

print(x)
print(y)
print("Is int number bigger than float number?")
if x > y:
    print('True')
else:
    print('False')