import random

def random_trivia():
    trivia = [{"question" : "When did Facebook first launch?",
               "answer" : 2004},

               {"question" : "How many Harry Potter books are out there?",
                "answer" : 7},

                {"question" : "How many herbs and spices are in Colonel Sanders' original KFC recipe?",
                 "answer" : 11}]
    
    trivias = random.choice(trivia)
    question = trivias["question"]
    answer = trivias["answer"]

    return question, answer



def main(): 
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
            
    #Payment
                
        print(f"That would be ${Price}")

        while True:
            Pay = float(input("Insert Cash: $"))

            if Pay < Price:
                print("THAT IS NOT ENOUGH!")
            else:
                break
        
    #Trivia Game
            
        game = input("Please wait while we ready your item. Would you like to play a game of trivia while you wait? Y or N \n")

        if game.title() == "Y":
            print("If you get the question correctly, your item will be free of charge.\n")
            trivia = random_trivia()
            question, answer = trivia

            print(question)

            answered = int(input("Input answer: "))
            if answered == answer:
                print("\nTING TING TING! YOU ARE CORRECT. ENJOY YOUR FREE ITEM!")
                print(f"Here is your money back: ${Pay}")
            else:
                print("\nCongratulations! That is wrong :((")
                change = float(Pay - Price)
                print(f"Here is your change: ${change}\n")

     #Display the item   
        for key, value in Menu.items():
            if key == order:
                print(f"Your {value} has been dispersed.\n")

    #Ask if they want more
                
        more = input("Would you like anything else? Y or N \n")

        if more.title() == "Y":
            order = ""
            continue
        else:
            break

    #End the program
    print("Thank you for coming!")

main()