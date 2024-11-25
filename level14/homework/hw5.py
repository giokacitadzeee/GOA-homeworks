#5)შეამოწმეთ, თუ ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე.

#first we have to add variable for number

number = int(input("give me a number: "))

#now we will use if, and, or functions for algorithm
if number > 10 and number < 50:
    print("number is more than 10 and is less than 50")
elif number < 10 or number > 50:
    print("number is less than 10 or more than 50")