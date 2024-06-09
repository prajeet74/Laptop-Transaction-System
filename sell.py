import readfile
import display
from datetime import datetime
def sell():
    laptop_dictionary = readfile.dictionary()
    print("-------------------------------------------------------------------------------------------------------------")
    print("For Bill Generation you will have to enter the customer's details first: ")
    print("\n")
    while True:
        try:
            name = input("Enter customer's name: ")
            if not name.isalpha():
                raise ValueError
            break
        except ValueError:
            print("Please input name in String format")
        print("\n")
    
    phone_number = int(input("Enter customer's number: "))
    print("\n")
    user_purchased_laptops = []
    want_more_laptop=True
    while want_more_laptop==True:
        display.display()
        # print("S.N.  \tName\t\t Brand\t\t Price \t\t Quantity \t Processor\t Graphic Card")
        
        # file = open("laptop.txt","r")
        # a = 1
        # for line in file:
        #     print(a,"\t"+line.replace(",","\t"))
        #     a = a + 1
        # print("---------------------------------------------------")
        # file.close()
        print("\n") 
        valid_id=int(input("Give the ID of the laptop that the customer wants to purchase: "))
        print("\n")

        #Valid ID
        while valid_id<=0 or valid_id>len(laptop_dictionary ):
            print("Please provide a valid Laptop ID !!!")
            print("\n")
            valid_id=int(input("Give the ID of the laptop that the customer wants to purchase: "))

        user_quantity=int(input("Please provide the quantity of the laptop that the customer want to purcahase: "))
        print("\n")
            
            #Valid Quantity
        get_quantity = laptop_dictionary [valid_id][3]
        while user_quantity <= 0 or user_quantity > int(get_quantity):
            print("Dear Admin, the quantity you looking for is not available ")
            print("\n")
            user_quantity = int(input("Please Provide the number of quantity of laptop "))
            print("\n")
        
        # update the text file 
        laptop_dictionary [valid_id][3]=int(laptop_dictionary [valid_id][3])-int(user_quantity)
        
        with open("laptop.txt","w") as file:
            for values in laptop_dictionary .values():
                file.write(str(values[0]+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5])))
                file.write("\n")
            
            
        # getting user purchased items
        name_of_product = laptop_dictionary [valid_id][0]
        quantity_selected_by_user = user_quantity
        
        # unit_price = laptop_dictionary [valid_id][2]
        price_of_selected_item = laptop_dictionary [valid_id][2].replace("$",'')
        total_price = int(price_of_selected_item)*int(quantity_selected_by_user)

        more_laptops=input("Do you want to purchase more laptops?(Y/N): ").upper()
        if more_laptops=="Y":
            want_more_laptop=True
        elif more_laptops=="N":
            want_more_laptop=False
        

        # user_purchased_laptops = []
        user_purchased_laptops.append([name_of_product, quantity_selected_by_user, price_of_selected_item, total_price])
    shipping_cost = input ("Dear user do you want your laptop to be shipped?(Y/N) ").upper()
    if shipping_cost == "Y":
        shipping_cost = 500
    elif shipping_cost == "N":
        shipping_cost = 0
        
    total = 0
    grand_total = 0
    for i in user_purchased_laptops:
        total+= int(i[1])*int(i[2])
        grand_total = total + shipping_cost
        today_date_and_time = datetime.now()
    print("/n")
    print("\t \t \t \t laptop Shop Bill")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255")
    print("\n")
    print("----------------------------------------------------------")
    print("Laptop deatils are:")
    print("----------------------------------------------------------")
    print("Name of the Customer: "+str(name))
    print("Contact number: "+str(phone_number))
    print("Date and time of purchase: "+str(today_date_and_time),)
    print("----------------------------------------------------------")
    print("\n")
    print("Purchase Detail are:")
    print("------------------------------------------------------------------------------------------")
    print("Items Name \t\t Total Quantity \t\t Unit Price \t\t Total")
    print("-----------------------------------------------------------------------------------------------------------")
    for i in user_purchased_laptops:
            print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
    print("-----------------------------------------------------------------------------------------------------------")
        
    print("Shipping Cost:$", shipping_cost)
            
    print("Grand Total:$" + str(grand_total))
    return user_purchased_laptops,today_date_and_time,grand_total,total,name,phone_number,shipping_cost
