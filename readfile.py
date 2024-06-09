def dictionary():
    file = open("laptop.txt", "r")
    mydict = {}
    laptop_id = 1
    for line in file:
        line = line.replace("\n","")
        mydict.update({laptop_id:line.split(",")})
        laptop_id+=1 
    return (mydict)