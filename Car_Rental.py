from difflib import get_close_matches
from colorama import Fore
from tinydb import *
from datetime import *
from os import system

def CarRent():
    try:
        def ShowServices(n): 
            try:
                print(Fore.GREEN + "\nSevices Available:-" + Fore.RESET)
                
                print(Fore.GREEN + '''
                1. Display Cars available.
                2. Rent a Car.
                3. Return Rented Car.
                4. Show Customer details.
                5. Exit.''' + Fore.RESET)

                s = int(input(Fore.YELLOW + "Enter Option to access the Services: " + Fore.RESET))
                return service(n,s)
            except ValueError:
                print(Fore.RED + "\nOptions entered should be integers" + Fore.RESET)
                return ShowServices(n)

        def service(n,s):
            db = TinyDB("Your json file path")
            user = Query()

            if s == 1:
                return CurrentCar(n,k)
        
            elif s == 2:
                rec =  db.search((user.Name == n))
                
                if rec[0]["Car"] == "No Car rented":
                    w = int(input(Fore.YELLOW + "\nPlease Check Cars available if not. To dispaly cars available enter 0 else 1 to continue. Enter 2 to return to Services' menu: " + Fore.RESET))
                    return Rent(n, w)
                
                else:
                    print(Fore.RED + "\nOnly 1 car can be rented on each Aadhar Number." + Fore.RESET)
                    
                    input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                    return ShowServices(n)
        
            elif s == 3:
                rec =  db.search((user.Name == n))
                
                if rec[0]["Car"] == "No Car rented":
                    print(Fore.RED + "\nService not Available." + Fore.RESET)
                    
                    input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                    return ShowServices(n)
                
                else:
                    rentedCar(n)
        
            elif s == 4:
                userDetails(n)

            elif s == 5:
                print(Fore.GREEN + '\nThanks for using our Services\n' + Fore.RESET)
                system('cls') 
                return CarRent()

            else:
                c = int(input(Fore.RED + "\nEnter correct Options: " + Fore.RESET))
                return service(n,c) 
            


        def CurrentCar(n, k):
            f = open("Path of text file where you have list of cars available to rent", "r")
            
            print(Fore.CYAN + "\nCars available are:-\n",f.read(),sep ='')
            
            input(Fore.GREEN + "\nPress Enter to continue.\n" + Fore.RESET)
            
            if k == 1:
                return Rent(n, 1)
            
            else:
                return ShowServices(n)


        def Rent(n, w):
            try:
                if w == 0:
                    k = 1
                    return CurrentCar(n, k)
            
                elif w == 1:
                    car = input(Fore.YELLOW + "\nEnter Car Name to continue else 1 to return to Services' menu: " + Fore.RESET)
                    
                    if car == '1':
                        return ShowServices(n)
                    
                    else:    
                        f = open("Path of text file where you have list of cars available to rent", "r")
                        find = f.read()
                        return Pay(car, find, n)

                elif w == 2:
                    return ShowServices(n)
            
                else:
                    c = input(Fore.RED + "\nEnter correct Options: " + Fore.RESET)
                    return Rent(n, c)
            
            except ValueError:
                print(Fore.RED + "\nOptions entered should be integers\n" + Fore.RESET)
                w = int(input(Fore.RED + "\nPlease Check Cars available if not. To dispaly cars available enter 0 else 1 to continue. Enter 2 to return to Services' menu: " + Fore.RESET))
                return Rent(n, w)


        def Pay(car,find, n):  
            if car in find:
                day = int(input(Fore.YELLOW + "\nEnter no. of days: " + Fore.RESET))
                returnDay = str(date.today() + timedelta(days=day))

                if day <= 15 and day >= 1:
                    bill = day*2000 + 2000
                    confirm = input(Fore.RED + "\nWrite 'CONFIRM' to cofirm booking: \n" + Fore.RESET).upper()
                
                    if confirm == "CONFIRM":
                        print(Fore.RED + "\nBooking Confirmed. Bill:" + Fore.RESET, " ₹", bill, sep='')
                        print(Fore.RED + "\nDate to return Car:" + Fore.RESET, returnDay)
                        input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                
                    else:
                        return Pay(car, find, n)
                    return afterPay(car, n, returnDay)
                
                elif day > 15:
                    bill = day*1800 + 2000
                    confirm = input(Fore.RED + "\nWrite 'CONFIRM' to cofirm booking: " + Fore.RESET).upper()
                
                    if confirm == "CONFIRM":
                        print(Fore.RED + "\nBooking Confirmed. Bill:" + Fore.RESET, " ₹", bill, sep='')
                        print(Fore.RED + "\nDate to return Car:" + Fore.RESET, returnDay)
                        input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                
                    else:
                        return Pay(car, find, n)
                    return afterPay(car, n, returnDay)
                
                else:
                    print(Fore.RED + "\nNo. of days should be greater than 0\n" + Fore.RESET) 
                    return Pay(car, find, n)
            else:
                l = []
                f = open("Path of text file where you have list of cars available to rent","r")
                
                for cars in f:
                    l.append(cars.strip())
                close = get_close_matches(car,l)
            
                print(Fore.RED + "\nIs car name:" + Fore.RESET,close)
                
                c = input(Fore.YELLOW + "\nEnter Yes(Y) or No(N): " + Fore.RESET)
                
                if c == 'Y' or c == 'y':
                    car = car.join(close)
                    return Pay(car, find, n)
                
                elif c == 'N' or c == 'n':
                    print(Fore.RED + "\nAgain enter car name\n" + Fore.RESET)
                    return CurrentCar(n,1)
                
                else:
                    print(Fore.RED + "\nRespond with Y or N\n" + Fore.RESET)
                    return Pay(car, find, n)
            

        def afterPay(car, n, returnDay):    
            f = open("Path of text file where you have list of cars available to rent", "r")
            fremove = f.readlines()
            f = open("Path of text file where you have list of cars available to rent", "w")
            
            for AvaiCar in fremove:
                if AvaiCar.strip("\n") != car:
                    f.write(AvaiCar)
            f.close()
            
            f1 = open("Path of text file where you have list of cars that are rented", "a")
            f1.write(car+"\n")
            f1.close()

            db = TinyDB("Your json file path")
            user = Query()
            db.update({"Date" : returnDay}, user.Name == n)
            db.update({"Car" : car}, user.Name == n)

            return ShowServices(n)


        def rentedCar(n):
            car = input(Fore.YELLOW + "\nEnter Rented Car Name: " + Fore.RESET)
            f = open("Path of text file where you have list of cars that are rented", "r")
            find = f.read()
            return returnCar(car, find, n)


        def returnCar(car, find, n):
            db = TinyDB("Your json file path")
            user = Query()
            
            if car in find:
                rec =  db.search((user.Name == n))
                chkDate = rec[0]["Date"]
                
                if str(date.today()) > chkDate:
                    print(Fore.RED + "\nCar returned past due date.\n" + Fore.RESET)
                
                if rec[0]["Car"] == car:
                    print(Fore.GREEN + "\nCar returned successfully. Your refund will be proceeded after inspection of car\n" + Fore.RESET)
                    f = open("Path of text file where you have list of cars that are rented", "r")
                    fremove = f.readlines()
                    f = open("Path of text file where you have list of cars that are rented", "w")
                    
                    for RentCar in fremove:
                        if RentCar.strip("\n") != car:
                            f.write(RentCar)
                    f.close()

                    f = open("Path of text file where you have list of cars that are rented", "r")
                    f1 = open("Path of text file where you have list of cars available to rent", "a")
                    f1.write("\n")
                    f1.write(car)
                    f1.close()

                    db = TinyDB("C:\\Users\\Aditya\\Desktop\\Car Rental\\User.json")
                    user = Query()
                    db.update({"Car" : "No Car rented"}, user.Name == n)
                    db.update({"Date" : "No due date"}, user.Name == n)
                    input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                    return ShowServices(n)
                
                else:
                    print(Fore.RED + "\nEntered car is not rented by you. Please enter car name again.\n" + Fore.RESET)
                    return rentedCar(n)
            
            else:
                l = []
                f = open("Path of text file where you have list of cars that are rented","r")
                
                for RentCar in f:
                    l.append(RentCar.strip())
                close = get_close_matches(car, l)
                
                print(Fore.RED + "\nIs car name: " + Fore.RESET,close)
                
                c = input(Fore.YELLOW + "\nEnter Yes(Y) or No(N): " + Fore.RESET)
            
                if c == 'Y' or c == 'y':
                    car = car.join(close)
                    return returnCar(car, find, n)
            
                elif c == 'N' or c == 'n':
                    print(Fore.RED + "\nAgain enter car name\n" + Fore.RESET)
                    return rentedCar(n)
            
                else:
                    print(Fore.RED + "\nRespond with Y or N\n" + Fore.RESET)
                    return returnCar(car, find, n)


        def userDetails(n):
            db = TinyDB("Your json file path")
            user = Query()
            rec =  db.search((user.Name == n))
            print(Fore.GREEN + "\nCustomer Details:-" + Fore.RESET)
            print(Fore.GREEN + "Name:" + Fore.RESET, n)
            print(Fore.GREEN + "Aadhar Number:" + Fore.RESET, rec[0]["Aadhar"])
            print(Fore.GREEN + "Mobile Number:" + Fore.RESET,rec[0]["Mobile"])
            print(Fore.GREEN + "Car currently rented:" + Fore.RESET, rec[0]["Car"])
            print(Fore.GREEN + "Due Date:" + Fore.RESET, rec[0]["Date"])

            chkDate = rec[0]["Date"]
            if str(date.today()) > chkDate:
                print(Fore.RED + "\nCar returned past due date.\n" + Fore.RESET)

            input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
            return ShowServices(n)


        def RegisterUser():
            db = TinyDB("Your json file path")
            user = Query()
            
            Name = input(Fore.YELLOW + "\nEnter Full Name: " + Fore.RESET)

            k = 0
            while k != 1:
                try:
                    mobile = int(input(Fore.YELLOW + "\nEnter Mobile Number: " + Fore.RESET))
                    if (len(str(mobile)) > 10) or (len(str(mobile)) < 10):
                        print(Fore.RED + "\nMobile Number must be of 10 digits.\n")
                        mobile = int(input(Fore.RED + "\nEnter Mobile Number: " + Fore.RESET))
                    
                    elif db.get(user.Mobile == mobile):
                        print(Fore.RED + "\nCustomer already exist\n" + Fore.RESET)
                        input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                        system('cls')
                        return CarRent()
                    
                    else:
                        k = 1
                
                except ValueError:
                    print(Fore.RED + "\nMobile Number must be of 10 digits and an integer\n" + Fore.RESET)
                    mobile = int(input(Fore.RED + "\nEnter Mobile Number: ") + Fore.RESET)
            

            k = 0
            while k != 1:
                try:
                    Ano = int(input(Fore.YELLOW + "\nEnter Aadhar Number: " + Fore.RESET))
                    
                    if (len(str(Ano)) > 12) or (len(str(Ano)) < 12):
                        print(Fore.RED + "\nAadhar Number must be of 12 digit.\n")
                        Ano = int(input(Fore.RED + "\nEnter Aadhar Number: " + Fore.RESET))
                    
                    elif db.get(user.Aadhar == str(Ano)):
                        print(Fore.RED + "\nCustomer already exist\n" + Fore.RESET)
                        input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                        system('cls')
                        return CarRent()
                    
                    else:
                        k = 1
                        Ano = str(Ano) 
                
                except ValueError:
                    print(Fore.RED + "\nAadhar Number must be of 12 digits and an integer\n" + Fore.RESET)
                    Ano = int(input(Fore.RED + "\nEnter Aadhar Number: ") + Fore.RESET)

            db.insert({
                "Name" : Name,
                "Aadhar" : Ano,
                "Mobile" : mobile,
                "Car" : "No Car rented",
                "Date" : "No due date"})
            
            print(Fore.RED + "\nCustomer Registered.\n" + Fore.RESET)
            print(Fore.GREEN + "\nCustomer Details:-" + Fore.RESET)
            print(Fore.GREEN + "Name:" + Fore.RESET,Name)
            print(Fore.GREEN + "Aadhar Number:" + Fore.RESET,Ano)
            print(Fore.GREEN + "Mobile Number:" + Fore.RESET,mobile)
            print(Fore.GREEN + "Car currently rented:" + Fore.RESET, "No Car rented")
            print(Fore.GREEN + "Due Date:" + Fore.RESET, "No due date")
            input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
            return Ano


        def RegisteredUser():
            db = TinyDB("Your json file path")
            user = Query()
            
            Ano = input(Fore.YELLOW + "\nEnter Aadhar Number: " + Fore.RESET)
            
            rec =  db.search(user.Aadhar == Ano)
            
            if (rec):
                print(Fore.GREEN + "\nCustomer Details:-" + Fore.RESET)
                print(Fore.GREEN + "Name:" + Fore.RESET, rec[0]["Name"])
                print(Fore.GREEN + "Aadhar Number:" + Fore.RESET, Ano)
                print(Fore.GREEN + "Mobile Number:" + Fore.RESET,rec[0]["Mobile"])
                print(Fore.GREEN + "Car currently rented:" + Fore.RESET, rec[0]["Car"])
                print(Fore.GREEN + "Due Date:" + Fore.RESET, rec[0]["Date"])
                
                chkDate = rec[0]["Date"]
                if str(date.today()) > chkDate:
                    print(Fore.RED + "\nReturn Date is past due date.\n" + Fore.RESET)
                
                input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                return Ano
            
            else:
                print(Fore.RED + "\nCustomer not found. Aadhar Number must be of 12 digits and an integer." + Fore.RESET)
                input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)

                system('cls')
                return CarRent()


        print("\t"*5, Fore.RED + "-"*20,"Welcome to Car Rents Pvt Limited","-"*20 + Fore.RESET)

        print(Fore.GREEN + """
        Price:
        ₹2000 per day if car is booked for less than or equal to 15 days + ₹2000 Caution Money.
        ₹1800 per day if car is booked for more than 15 days + ₹2000 Caution Money.\n""" + Fore.RESET,
        Fore.LIGHTRED_EX + """
        1. Caution Money includes damages to vehicle and late return of vehicle and will be 
           refunded after complete inspection of rented vehicle.
        2. Only 1 car can be rented on each Aadhar Number.
        3. Press Ctrl + C to exit at any moment.
        """ + Fore.RESET)

        input(Fore.CYAN + "Press Enter to continue.\n" + Fore.RESET)

        Customer = input(Fore.YELLOW + "\nAre you registerd customer?(Y/N): " + Fore.RESET)

        if (Customer == 'Y') or (Customer == 'y'):
            n = RegisteredUser()

        elif (Customer == 'N') or (Customer == 'n'):
            n = RegisterUser()

        else:
            print(Fore.RED +  "\nRespond with Y or N\n" + Fore.RESET)
            system('cls')
            return CarRent()

        k = 0
        ShowServices(n)
    
    except KeyboardInterrupt:
        exit()

system('cls')
CarRent()