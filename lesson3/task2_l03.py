from random import uniform

rand_num1 = uniform(1, 100)
rand_num2 = uniform(1, 100)
mul = rand_num1 * rand_num2
print('Multiplication without rounding:', mul)
print('Multiplication with rounding:', round(mul,4))
print('Multiplication with rounding:', round(mul,2))                   