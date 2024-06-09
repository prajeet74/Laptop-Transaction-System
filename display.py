def display():
    print("S.N.  \tName\t\t Brand\t\t Price \t\t Quantity \t Processor\t Graphic Card")
    a = 1
    with open("laptop.txt","r") as file:
        for line in file:
            print(a,"\t"+line.replace(",","\t"))
            a = a + 1
        