
# a = 5
# b = "10"
# result = a + b
# print("Result:", result)

#კოდი გამოიტანს ერორს დაწერეთ რატომ და ასევე ცალკე დაწერეთ სწორი ფორმა 

#since it is impossible to do operations between int and string we cant concatination them so we have to fix it by making b also an int like it is in bellow

a = 5
b = "10"
result = a + int(b)
print("Result:", result)