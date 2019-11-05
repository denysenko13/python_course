from random import randint

rand_num = randint(1, 50)
pow_num = pow(rand_num, 2)
print("Random number:", rand_num, "\nPower from number:", pow_num)
print("Is number is bigger than 10?", rand_num > 10)
print("Is power from number is bigger than 500?", pow_num > 500)