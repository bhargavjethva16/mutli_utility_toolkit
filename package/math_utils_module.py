


from datetime import datetime
from time import time, sleep
import time
import math
import random
import string
from uuid import uuid4

def dt_operations():
    while True:
        
        print()
        print("Datetime and Time Operations:")
        print()
        print("1. Display current data and time")
        print("2. Calculate difference between two dates/times" )
        print("3. Format data into custom ")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        print()

        option = int(input("Choose your option:- "))

        if option == 1 :
            
            print(f" Current Date and Time: {datetime.now()}")

        elif option == 2 :
            
            print()
            start = input("Enter the first date  (YYYY-MM-DD): ")
            end  = input("Enter the second date  (YYYY-MM-DD): ")

            dt1 = datetime.strptime(start,"%Y-%m-%d")
            dt2 = datetime.strptime(end,"%Y-%m-%d")
            print()
            print(f"Difference: {abs(dt2-dt1)}")

        elif option == 3:
            
            print("1. Date")
            print("2. Time")
            print("3. Date-Time")


            choice = int(input("Enter your choice:- "))

            if choice == 1 :
               
                print(f"Current Date: {datetime.now().date()}")

            elif choice == 2 :
               
                print(f"Current Time: {datetime.now().time()}")

            elif choice == 3 :
               
                print(f"Current Date-Time: {datetime.now()}")


        elif option == 4 :
          
            start = time.time()
            input("Enter for Stop Watch:- ")
            end  =  time.time()
            print(f"Total time : {end-start}")


        elif option == 5 :
          
            count = int(input("Enter a time: "))

            for i in range(count, 0, -1):
                print(i)
                time.sleep(1)

        elif option == 6 :
          
            print("Exiting")
            break
        else:
            print("Enter valid Choice")


def math_operations():
    
    print()
    print("--------- Mathematical Operations -----------")
    print("1. Calculate Factorial")
    print("2. Solve Compound Interest")
    print("3. Trigonometric Calculations")
    print("4. Area of Geometric Shapes")
    print("5. Back to Main Menu")
    print()

    choice = int(input("Enter your Choice:- "))

    if choice == 1 :
       
        num = int(input("Enter Number: "))
        print(math.factorial(num))
        

    elif choice == 2 :
        
        money = float(input("Enter Amount: "))
        interest = float(input("Enter Rate of Interest: "))
        year = float(input("Enter Time Duration: "))

        f = money*(1+interest/100)**year
        print(f"Compound Interest for given Amount {money} with Rate of Interest {interest} for Time Duration {year} is : {f}")


    elif choice == 3 :
        
        num  = float(input("Enter degree:-  "))
        num = math.radians(num)
        print(math.cos(num))
        print(math.sin(num))


    elif choice == 4 :
        while True:
            
            print()
            print("1. Area of Circle")
            print("2. Area of Square")
            print("3. Area of Rectangle")
            print("4. Back to Main Menu")

            ch = int(input("Enter your choiceL:-  "))

            print()
            
            if ch == 1: 
                
                rad = float(input("Enter Radius Value:-  "))
                area = math.pi*rad*rad
                print(f"Area of Circle with given Radius {rad} : {area}")

            
            elif ch == 2 :
                
                s = float(input("Enter the 1-side-length of square:- "))
                area_squa = s*s
                print(f"Area of Square with given Side-Length {s} : {area_squa}")

            
            elif ch == 3 :
                
                len = float(input("Enter the Length (L) :-  "))
                wid = float(input("Enter the Width (W) :-  "))
                area = len*wid
                print(f"Area of the Rectangle with given length[{len}] and width[{wid}] : [Area = ( {len} x {wid} = {area}) ]")

            elif ch == 4 :
                print("Going to main menu")
                return


    elif choice == 5 :
        print("Going to main menu")
        return

def random_operations():
    print()
    print("--------- Random Number Operations -----------")
    print("1. Generate Random Number")
    print("2. Generate Random List")
    print("3. Shuffle a List")
    print("4. Generate Random OTP")
    print("5. Back to Main Menu")
    print()

    choice = int(input("Enter your Choice:- "))

    if choice == 1:
        num= random.randint(1, 100)
        print(f"Random Number  {num}")

    elif choice == 2:
        lst =[ 12, 34, 56, 78, 90]
        random.shuffle(lst)
        print(f"Random List: {lst}")

    elif choice == 3:
        length = int(input("Enter the length of the password: "))
        value = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(value,k=length) )
        print(f"Generated Password: {password}")

    elif choice == 4:
        num = random.randint(100000, 999999)
        print(f"Generated Random OTP is : {num}")

    elif choice == 5:
        print("Going to main menu")
        return

    else:
        print("Enter valid choice")

def uuid_operations():
    print()
    print("--------- UUID Operations -----------")
    print("1. Generate UUID")
    print("2. Back to Main Menu")
    print()

    choice = int(input("Enter your Choice:- "))

    if choice == 1:
        unique_id = uuid4()
        print(f"Generated UUID: {unique_id}")

    elif choice == 2:
        print("Going to main menu")
        return

    else:
        print("Enter valid choice")
        








