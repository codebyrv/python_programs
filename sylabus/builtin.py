
numbers = []



def display():
    print("Current list:", numbers)



def add(value):
    numbers.append(value)
    print("Element added successfully")

def delete():
    if len(numbers) > 0:
        value = numbers.pop()
        print("Deleted element:", value)
    else:
        print("List is empty")

def search(value):
    if value in numbers:
        print("Element found")
    else:
        print("Element not found")

def average():
    if len(numbers) > 0:
        avg = sum(numbers) / len(numbers)
        print("Average =", avg)
    else:
        print("List is empty")

n = int(input("Enter the number of elements: "))

for i in range(n):
    val = int(input("Enter the element: "))
    numbers.append(val)



while True:

    
    print("1. Display")
    print("2. Add")
    print("3. Delete")
    print("4. Search")
    print("5. Average")
    print("6. Maximum")
    print("7. Minimum")
    print("8. Length")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display()

    elif choice == 2:
        val = int(input("Enter the element to add: "))
        add(val)

    elif choice == 3:
        delete()

    elif choice == 4:
        val = int(input("Enter the element to search: "))
        search(val)

    elif choice == 5:
        average()

    elif choice == 6:
        if len(numbers) > 0:
            print("Maximum =", max(numbers))
        else:
            print("List is empty")

    elif choice == 7:
        if len(numbers) > 0:
            print("Minimum =", min(numbers))
        else:
            print("List is empty")

    elif choice == 8:
        print("Length =", len(numbers))

    elif choice == 9:
        print("Program exited successfully")
        break

    else:
        print("Invalid choice")
