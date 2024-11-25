#2) გამოიყენეთ or ოპერატორი, რათა შეამოწმოთ, თუ მოცემული ციფრები არიან 10-ზე 
# მეტი ან 50-ზე ნაკლები.

age = int((input("tell me your age")))

if age > 10 and age < 50:
    print("your age is more than 10 and less than 50")
if age <= 10 or age >=50:
    print("your age is either not more than 10 or is more than 50")