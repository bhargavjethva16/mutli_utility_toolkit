from package import dt_operations
from package import dir_operations
from package import file_operations
from package import math_operations, random_operations, uuid_operations


while True:
    print()
    print("=======================================")
    print("\nWelcome to Multi-Utility Toolkit")
    print("\n=======================================")
    print()


    print("Choose an option-")
    print()     
    print("1. Datetime and Time Operations")     
    print("2. Mathematical Operations")     
    print("3. Random Data Generation")     
    print("4. Generate Unique Identifiers (UUID)")     
    print("5. File Operations (Custom Module)")     
    print("6. Explore Module Attributes (dir())")     
    print("7. Exit")     
    print()     
    print("===========================================")     
    print()     


    choice = int(input("Enter your choice:-  "))

    if choice == 1:
        dt_operations()
    elif choice == 2:
        math_operations()
    elif choice == 3:
        random_operations()
    elif choice == 4:
        uuid_operations()
    elif choice == 5 :
        file_operations()   
    elif choice == 6 :
        dir_operations()
    elif choice == 7 :
        print("Exiting the program")
        break
    else:
        print("Enter valid Choice")

