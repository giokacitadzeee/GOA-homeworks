#1)მომხმარებელს შემოატანანინეთ ორი რიცხვი და მათზე მოახდინეთ მათემატიკური ოპერაციები
number1 = float(input("tell me a number:"))
number2 = float(input("tell me second number: "))
mathematical_opperation = input("give me mathematical opperation(+, -, *, /, 2):")

if mathematical_opperation == ("+"):
    print(number1 + number2)
elif mathematical_opperation == ("-"):
    print(number1 - number2)
elif mathematical_opperation == ("*"):
    print(number1 * number2)
elif (mathematical_opperation) == ("/"):
    print(number1 / number2)
elif(mathematical_opperation) == ("2"):
    print((number1 * number1) , (number2 * number2))