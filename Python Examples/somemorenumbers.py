import random
try:
    number = int(input("Pick a random fucking number between 1 and what:"))
except ValueError:
    print("You fucked up! Now you get my number: 69")
    number = 69
random_number1 = random.randint(1, number)
random_number2 = random.randint(1, number)
random_number3 = random.randint(1, number)
random_number4 = random.randint(1, number)
random_number5 = random.randint(1, number)
random_number6 = random.randint(1, number)
print("Your fucking numbers are: ", random_number1, random_number2, random_number3, random_number4, random_number5, random_number6)
