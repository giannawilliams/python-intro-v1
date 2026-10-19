number = float(input("Enter a number: "))
if number%2 == 0:
    parity = "even"
else:
    parity = "odd"
if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "positive"

print(f"{number} is {parity}.")
print(f"{number} is {sign}.")