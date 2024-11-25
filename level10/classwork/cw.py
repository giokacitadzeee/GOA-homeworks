# input - შეყვანა
# output - გამოტანა


# name = input("Enter Your Name: ")
# print(name)

# 1) მომხმარებელს შეეკითხეთ სახელი შემდეგ კი მას მიესალმეთ ქართულად გამარჯობა სახელი

# name = input("whats your name")
# print("გამარჯობა " + name)



# number1 = int(input("number:"))
# number2 = int(input("number:"))

# print(number1 + number2)

# num = int(input("რამდენი წლით გსურს დროში მოგზაურობა: "))

# print(str(num) + "წლის შემდეგ იქნება" + str(2024 + num))


#მომხამრებელს შემოატანინეთ ახლანდელი ასაკი ასევე შემოატანინეთ ახლანდელი წელი, შემდეგ შეეკითხეთ რამდენი წლით სურს დროში მოგზაურობა შემდეგ კი დაბეჭდეთ ერთ გრძელ წინადადებაში რამდენი წლის იქნება მომხარებელი დროში მოგზაურობის შემდეგ და რომელი წელიწადი იქნება დროში მოგზაურობის შემდეგ

current_age = int(input("how old are you? "))
current_year = int(input("which year it is now? "))
time_machine = int(input("how many years do you want to skip?"))

print("in " + str(time_machine) + " years you are going to be " + str(int(current_age + time_machine)) + " years old and its gonna be " + str(int(current_year + time_machine)))
