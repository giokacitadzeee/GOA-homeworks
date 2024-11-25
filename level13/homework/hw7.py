#7) მომხმარებელს შემოატაინეთ 2 რიცხვი, და შემდეგ გამოიყენეთ შედარების 
# ოპერატორები რა რიცხვსაც შეიყვანს მომხმარებელი, 
# მასე გამოიყენთ შედარების ოპერატორები ==,!=,<,>,<=,=>.
#calculator for comparison

number1 = input("tell me a number")
number2 = input("tell me second number")

if number1 > number2:
    print("number1 is higher than number2")
elif number1 < number2:
    print("number1 is lower than number2")
elif number1 == number2:
    print("number1 and number2 are equal")