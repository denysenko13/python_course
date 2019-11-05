number = int(input("Q: Enter the number\nA: "))
power = int(input("Q: Enter the power\nA: "))
result_1 = number ** power
result_2 = pow(number, power)
print("Result:", result_1, "Type **:")
print("Result:", result_2, "Type pow():")
print("Is result1 equal for result2?", result_1 == result_2)