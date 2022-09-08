def convert(gallons):
    litres = 3.78541178 * gallons
    return litres

userInput = float(input("Gallons?: (Negative number ends) "))

while userInput > 0:
    print(f"{userInput} gallons {convert(userInput):.3f} litres")
    print("")
    userInput = float(input("Gallons?: "))