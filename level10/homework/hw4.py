#სახელი და ასაკი
#დაწერე პროგრამა, რომელიც მომხმარებელს შემოატანინებს სახელს და გვარს და დაპრონტავს ამ ორ მონაცემს ასეთი ფორმატით: "თქვენი სახელია X ხოლო თქვენ ხართ Y წლის"

name = input("whats your name? ")
lastname = input("whats your last name?")
age = int(input("how old are you?"))

print("your name is " + name + " your lastname is " + lastname + "and you're " + str(int(age)) + " years old")