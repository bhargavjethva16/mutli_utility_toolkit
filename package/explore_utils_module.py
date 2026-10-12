def dir_operations():
    while True:
        print()
        print("1. Math Module")
        print("2. Random Module")
        print("3. String Module")
        print("4. UUID Module")
        print("5. Date/Time Module")
        print("6. Exit")

        option = int(input("Enter your choice:- "))

        if option == 1:
           import math
           print(f"Math Module: {dir(math)}")
        elif option == 2:
            import random
            print(f"Random Module: {dir(random)}")
        elif option == 3:
            import string
            print(f"String Module: {dir(string)}")
        elif option == 4:
            import uuid
            print(f"UUID Module: {dir(uuid)}")
        elif option == 5:
            import  datetime
            print(f"Date/Time Module: {dir(datetime)}")
            
        elif option == 6:
            print()
            print("Exiting")
            print()
            break
        else:
            print("Enter valid Choice")
            print()