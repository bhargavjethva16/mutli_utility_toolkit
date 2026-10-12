def file_operations():
    while True:
        print("1. Create a file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Exit")

        option = int(input("Enter your choice:- "))

        if option == 1:
            filename = input("Enter the filename to create: ")
            try:
                with open(filename, 'x') as file:
                    print(f"File {filename} created successfully.")
            except :
                print(f"File {filename} already exists.")

        elif option == 2:
            filename = input("Enter the filename to write: ")
            content = input("Enter the content to write: ")
            with open(filename, 'w') as file:
                file.write(content)
                print(f"Content written to {filename}.")

                print(f"File {filename} not found.")

        elif option == 3:
            filename = input("Enter the filename to read: ")
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    print(f"Content of {filename}:\n{content}")
            except  :
                print(f"File {filename} not found.")

        elif option == 4:
            filename = input("Enter the filename to append: ")
            content = input("Enter the content to append: ")
            with open(filename, 'a') as file:
                file.write(content)
                print(f"Content appended to {filename}.")

        elif option == 5:
            print("Exiting")
            break
        else:
            print("Enter valid Choice")