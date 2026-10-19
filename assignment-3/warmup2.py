age = int(input("Enter your age: "))
if age >= 65: #greater than or equal to 65
    print("You are a senior.")
elif age <= 64 and age >=18: #less than or equal to 64 and greater than or equal to 18
    category = "Adult"
    print("You are an adult.")
elif age <=17 and age >=13: #less than or equal to 17 and greater than or equal to 13
    print("You are a teen.")
else:
    print("You are a child.")


