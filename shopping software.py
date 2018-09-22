Chips, Biscuit, Chocolate, Toffee, Milk, Cheese = 0, 0, 0, 0, 0, 0
ChipsC, BiscuitC, ChocolateC, ToffeeC, MilkC, CheeseC = 0, 0, 0, 0, 0, 0
CostumerName = input("Please enter Costumer Name : ")
print("WELCOME!!!!!!!!", CostumerName,",Happy Shopping")
choice = input("Please enter product bought among Chips, Biscuit, Chocolate, Toffee, Milk, Cheese : ")
while choice != "Done" :
    if choice == "Chips" :
        Chips += 1
    elif choice == "Biscuit" :
        Biscuit += 1
    elif choice == "Chocolate" :
        Chocolate += 1
    elif choice == "Toffee" :
        Toffee += 1
    elif choice == "Milk" :
        Milk += 1
    elif choice == "Cheese" :
        Cheese += 1
    else :
        print("Please enter valid choice")
    choice = input("Please enter product bought among Chips, Biscuit, Chocolate, Toffee, Milk, Cheese : ")
        
ChipC = Chips * 3
BiscuitC = Biscuit * 2
ChocolateC = Chocolate * 4
ToffeeC = Toffee
MilkC = Milk * 30
CheeseC = Cheese * 45
TotalC = ChipC + BiscuitC + ChocolateC + ToffeeC + MilkC + CheeseC
print(" Items Bought       Amount       Price        Total Price",
          "\nChips              ", Chips,"           ""$3      ","   $", ChipC,
          "\nChocolate          ", Chocolate,"          ""$4      ","   $", ChocolateC,
          "\nBiscuit            ", Biscuit,"           ""$2      ", "   $",BiscuitC,
          "\nToffee             ", Toffee, "           ""$1      ","   $", ToffeeC,
          "\nMilk               ", Milk,   "           ""$30     ","   $", MilkC,
          "\nCheese             ", Cheese,"           ""$45     ", "   $",CheeseC )
print(" Total Bill is $", TotalC)
print(" Thank You for shopping", CostumerName, "  \n HAVE A NICE DAY!!!!")
 
