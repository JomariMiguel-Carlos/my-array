print ("**********      PROGRAMMED BY      **********")
print ("**********  CARLOS, JOMARI MIGUEL  **********")

array_ = [1, 2, 3, 4, 5, 5, 5, 8, 9, 20]
print("\nArray: ", array_)

while True:
    try:
        print("Menu:")
        print("1 -> Add an element")
        print("2 -> Insert an element")
        print("3 -> Modify an element")
        print("4 -> Delete an element")
        print("5 -> Arrange in ascending order")
        print("6 -> Arrange in descending order")
        print("7 -> Remove the last element")
        print("8 -> Sum of all elements")
        print("9 -> Minimum value of an element")
        print("10 -> Maximum value of an element")
        print("11 -> Exit")

        choice = int(input("\nWhat do you want to do? (1-10): "))
        if choice not in range(1, 12):
            raise ValueError

    except ValueError:
        print("\nInvalid.")

    else:
        if choice == 1:
            try:
                add_element = int(input("\nEnter the element you want to add: "))
            except ValueError:
                print("\nInvalid.")
            else:
                array_.append(add_element)
                print("\nThis is the new Array: ", array_)

        elif choice == 2:
            try:
                ins_element1 = int(input("\nEnter the element you want to insert: "))
                ins_element2 = int(input("Enter the index where you want to place: "))
            except ValueError:
                print("\nInvalid.")
            else:
                array_.insert(ins_element2, ins_element1)
                print("\nThis is the new Array: ", array_)

        elif choice == 3:
            try:
                mod_element1 = int(input("\nEnter the index you want to modify: "))
                mod_element2 = int(input("Enter the element you want to replace: "))
                if mod_element1 not in array_:
                    raise ValueError
            except ValueError:
                print("\nInvalid.")
            else:
                array_[mod_element1] = mod_element2
                print("\nThis is the new Array: ", array_)

        elif choice == 4:
            try:
                del_element = int(input("\nEnter the index you want to delete: "))
            except ValueError:
                print("\nInvalid.")
            else:
                array_.remove(array_[del_element])
                print("\nThis is the new Array: ", array_)

        elif choice == 5:
            array_.sort()
            print("\nThis is the new Array: ", array_)

        elif choice == 6:
            array_.sort(reverse=True)
            print("\nThis is the new Array: ", array_)

        elif choice == 7:
            array_.pop()
            print("\nThis is the new array:", array_)

        elif choice == 8:
            total = sum(array_)
            print("\nThis is the sum of all elements:", total)

        elif choice == 9:
            smallest = min(array_)
            print("This is the smallest value of element:", smallest)


        elif choice == 10:
            biggest = max(array_)
            print("This is the biggest value of element:", biggest)


        elif choice == 11:
            break