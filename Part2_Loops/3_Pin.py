# https://www.w3schools.com/python/python_while_loops.asp

# Write a program that keeps asking the user for a PIN code until they type 4321.
# The program must print "Wrong" for every incorrect attempt.
# When the user enters the correct PIN, print how many attempts it took.
#
# Sample output:
# PIN: 3245
# Wrong
# PIN: 1234
# Wrong
# PIN: 0000
# Wrong
# PIN: 4321
# Correct! It took you 4 attempts
#
# If the user gets it right on the first try:
# PIN: 4321
# Correct! It only took you one single attempt!


# Write your code here:
correct_pin = "4321"
attempts = 0
pin = input("PIN: ")
while pin != "4321":
    pin = input("PIN: ")
    attempts += 1

if attempts == 1:
    print("CORRECT ! It only took you one try")
else:
    print(f"Correct! It only took you {attempts} attempts")
