
import readfile
import display
import write

readfile.dictionary()
print("\n")
print("\t\t\t\t Welcome to ZEXTER INTERNATIONAL")
print("\t\t\t\t\t Address : Skill Lab")
print("\t\t\t----------------------------------------------------")
print("\t\t\t\tPlease select any of below option: ")
print("\t\t\t----------------------------------------------------")

continueLoop = True
while continueLoop == True:
    print("\n")
    print("Press 1 to sell to customer")
    print("Press 2 to buy from manufacturer ")
    print("press 3 to exit from program")
    print("\n")
    userinput = int(input("Press from the above mentioned option: "))


    if userinput == 1:
        display.display()
        write.sell_invoice()

    if userinput==2:
        display.display()
        write.buy_invoice()
    
    if userinput ==3:
        continueLoop = False

    else:
        ("Please press appropriate option ")
