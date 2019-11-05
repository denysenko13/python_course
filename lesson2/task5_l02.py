from random import randint

x = randint(1, 50)
print("Random number:", x, "\nPower from number:", pow(x, 2))
print("Is number is bigger than 10?", x > 10)
print("Is power from number is bigger than 500?", pow(x, 2) > 500)