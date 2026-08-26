value = int(input("Enter the unit:"))
if value <=100:
    print("Your bill is:", value*5)
elif value <=200:
    print("Your bill is:", 100*5 + (value-100)*7)
else:
    print("Your bill is:", 100*5 + 100*7 + (value-200)*10)
