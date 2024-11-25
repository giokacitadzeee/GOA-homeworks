#1) თუ ასაკი არის 18 ის ზემოთ ან 50 წლის ქვემოთ  ან თუ  ასაკი  ნაკლებია 18 ზე და 
# მეტია 50 ზე გამოტანეთ ის უნდა იყოს ან მოხუცი ან ახალგაზრდა

age = int(input("give me your age"))

if age > 18 and age < 50:
    print("youre adult")
elif age <= 18:
    print("youre kid")
elif age >= 50:
    print("youre old")