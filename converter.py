
print("Hi, this is a kilometer-miles converter program!")

while True:
    kilometers = int(input("Enter the number of kilometers you'd like to convert:"))

    miles = round(kilometers/1.609, 2)

    print(kilometers, "km converts to", miles, "miles.")

    choice = input("Would you like to try another conversion (y/n)?")
    if choice.lower() !="y" and choice.lower() != "yes":
        break



