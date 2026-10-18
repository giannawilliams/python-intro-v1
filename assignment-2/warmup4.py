favorite_number = float(input("What is your favorite number? "))
if favorite_number%2 == 0:
    print("Your favorite number is even!")
else:
    print ("Your favotite number is odd!")

# The original error message:
# line 2, in <module>
#     if favorite_number%2 == 0:
#        ~~~~~~~~~~~~~~~^~
# TypeError: not all arguments converted during string formatting

# What caused the error:
# The input entered wasn't first converted to a integer/float before
# mathematical operations were perfomed. Since a string can't be mathematically
# operated on, I got the error.

# How to fix the error:
# I simply fixed the error by converting the input to a float.
# OLD (Wrong): favorite_number = input("What is your favorite number? ")

# NEW (Correct): favorite_number = float(input("What is your favorite number? "))
