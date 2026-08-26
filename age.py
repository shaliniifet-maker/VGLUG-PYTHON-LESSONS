age = int(input("Enter your Age:"))
if age >= 18:
    print("You are eligible to vote.")
elif age == 17:
    print("You are eligible to apply for a voter ID.")
else:
    print("You are not eligible to vote.")
