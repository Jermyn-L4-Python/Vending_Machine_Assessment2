Price = 0
order = ""

name = input("What is your name? ")
capital = name.title()

print(f"\nHello {capital}, Welcome to my vending machine.\n")

while True:
    print("Please choose one: ")

    Menu = {"A148" : "Lays", 
            "A290" : "Kitkat", 
            "A123" : "Snickers", 
            "B143" : "Cheeetos", 
            "B239" : "CocaCola", 
            "A000" : "Water", 
            "C257" : "Orange Juice"}

    print(Menu)

    while order not in Menu:
        order = input("\nCode: ")
    

        if order == "A148":
            Price = float(5.20)

        elif order == "A290":
            Price = float(3.75)
        
        elif order == "A123":
            Price = float(3.75)
        
        elif order == "B143":
            Price = float(6.50)

        elif order == "B239":
         Price = float(4.75)

        elif order == "A000":
            Price = float(0.25)

        elif order == "C257":
            Price = float(4.25)

        else:
            print("Im sorry, we don't have that here.")
        

    print(f"That would be ${Price}")

    while True:
        Pay = float(input("Insert Cash: $"))

        if Pay < Price:
            print("THAT IS NOT ENOUGH!")
        else:
            break


    change = float(Pay - Price)

    for key, value in Menu.items():
        if key == order:
            print(f"Your {value} has been dispersed.")


    print(f"Here is your change: ${change}")

    more = input("Would you like anything else? Y or N \n")
    more2 = more.title()

    if more2 == "Y":
        order = ""
        continue
    else:
        break

print("Thank you for coming!")
