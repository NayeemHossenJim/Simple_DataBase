MyDB = dict()
while True :
    Command = input("*")
    if Command == "Add" :
        Car1 = input("Please Enter Your Car1 Name : ")
        Prize1 = input("Please Enter Your Car1 Prize : ")
        Car2 = input("Please Enter Your Car2 Name : ")
        Prize2 = input("Please Enter Your Car2 Prize : ")
        Car3 = input("Please Enter Your Car3 Name : ")
        Prize3 = input("Please Enter Your Car3 Prize : ")
        MyDB[Car1] = Prize1 
        MyDB[Car2] = Prize2 
        MyDB[Car3] = Prize3 
    elif Command == "Get" :
        Car = input("Please Enter Your Car name : ")
        print(MyDB.get(Car))
    elif Command == "Exit" :
        break
    else :
        print("Sorry Sir, Please Check Your Credentials !")