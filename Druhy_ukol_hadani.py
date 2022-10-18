import random
number = random.randint(0,11)
n = 0
while (number != n):
    n = int(input());
    if n == number:
        print("\nUhodl jsi\n");
    elif n != number:
        print("\nHádej znovu.\n");