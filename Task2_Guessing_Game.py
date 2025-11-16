import random
num1 = random.randint(1,100)
num2 = 0
tries1 = 0
while num2 != num1:
    data1 = input("enter number ")
    data2 = int(data1)
    num2 = data2
    tries1 = tries1 + 1
    if num2 > num1:
        print("too high")
    if num2 < num1:
        print("too low")
    if num2 == num1:
        print("correct")
print("tries = ", tries1)