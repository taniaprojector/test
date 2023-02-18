from random import randint
answerMenu = input("Hi, dear client.\nWhat would you like to order?\nPlease, enter all the dishes, separated by commas")
answerMenuItem = answerMenu.split(',')
print(f"—--Our cafe's menu includes---")
checkSum = 0
for i in answerMenuItem:
    price = randint(100, 500)
    print(i + f" .... {price} UAH")
    checkSum = checkSum + price
print(f"In total.........{checkSum} UAH")
