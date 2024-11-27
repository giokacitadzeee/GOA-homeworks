#3) შეადარეთ თქვენი ასაკი მომხმარებლის შემოტანილ ასაკს, თუ თქვენი ასაკი მეტია მომხმარებლის ასაკზე უთხარით რომ თქვენ მასზე დიდი ხართ, 
# თუ მასზე პატარა ხართ დაუპრინტეთ რომ მასზე პატარა ხართ და სხვა შემთხვევაში დაუპრინტეთ რომ ტოლები ხართ.

customer_age = int(input("how old are you"))
my_age = 19

if customer_age > my_age:
    print("youre older than me ")
elif customer_age < my_age:
    print("Im older than you")
else:
    print("we are same age")
