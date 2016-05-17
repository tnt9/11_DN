import random

lotto = []
i = 0

n = int(raw_input("How many numbers would you like to get? "))
while i < n:
    number = random.randint(1, 40)
    if number in lotto:
        i = i
    else:
        lotto.append(number)
        i += 1

print lotto
