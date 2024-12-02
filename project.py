import random

def main():
    print("Welcome to the Random Name Picker!")
    allNames = []
    availableNames = []
    pickHistory = []

    while True:
        print("\nMenu:")
        print("1. Add names to the list")
        print("2. View all names")
        print("3. View current available names")
        print("4. Pick a random name")
        print("5. Pick multiple random names")
        print("6. View pick history")
        print("7. Clear names list and history")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            allNames, availableNames = addNames(allNames, availableNames)
        elif choice == "2":
            displayAllNames(allNames)
        elif choice == "3":
            displayAvailableNames(availableNames)
        elif choice == "4":
            pickRandom(availableNames, pickHistory, allNames)
        elif choice == "5":
            pickMultiple(availableNames, pickHistory, allNames)
        elif choice == "6":
            displayPickHistory(pickHistory)
        elif choice == "7":
            clearData(allNames, availableNames, pickHistory)
        elif choice == "8":
            print("Thank you and Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def addNames(allNames: list, availableNames: list) -> tuple:
    print("\nEnter names (type 'done' to stop):")
    while True:
        name = input("> ").strip()
        if name.lower() == 'done':
            break
        elif name and name not in allNames:
            allNames.append(name)
            availableNames.append(name)
        elif not name:
            print("Name cannot be empty. Please enter a name.")
        else:
            print(f"{name} is already in the list.")
    return allNames, availableNames

def displayAllNames(allNames: list):
    if allNames:
        print("\nAll names entered:")
        for i, name in enumerate(allNames, 1):
            print(f"{i}. {name}")
    else:
        print("\nNo names available. Add names first.")

def displayAvailableNames(availableNames: list):
    if availableNames:
        print("\nCurrent available names (not picked yet):")
        for i, name in enumerate(availableNames, 1):
            print(f"{i}. {name}")
    else:
        print("\nNo available names. Add names first.")

def pickRandom(availableNames: list, pickHistory: list, allNames: list) -> None:
    if availableNames:
        name = random.choice(availableNames)
        availableNames.remove(name)
        pickHistory.append(name)
        print(f"\nRandomly picked: {name}")
    else:
        print("\nNo names available to pick from.")
        restart = input("Would you like to start with all the names again? (yes/no): ").lower()
        if restart == 'yes':
            availableNames[:] = allNames
            pickHistory.clear()
            print("Names list and pick history have been reset.")
        else:
            print("Action cancelled.")

def pickMultiple(availableNames: list, pickHistory: list, allNames: list) -> None:
    if availableNames:
        while True:
            try:
                numToPick = int(input(f"\nEnter the number of names to pick (1-{len(availableNames)}): "))
                if numToPick < 1 or numToPick > len(availableNames):
                    print("\nInvalid number. Please pick between 1 and the number of names available.")
                else:
                    pickedNames = random.sample(availableNames, numToPick)
                    for picked in pickedNames:
                        availableNames.remove(picked)
                    pickHistory.extend(pickedNames)
                    print(f"\nRandomly picked names: {', '.join(pickedNames)}")
                    break
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
    else:
        print("\nNo names available to pick from.")
        restart = input("Would you like to start with all the names again? (yes/no): ").lower()
        if restart == 'yes':
            availableNames[:] = allNames
            pickHistory.clear()
            print("Names list and pick history have been reset.")
        else:
            print("Action cancelled.")

def displayPickHistory(pickHistory: list):
    if pickHistory:
        print("\nPick History:")
        for i, name in enumerate(pickHistory, 1):
            print(f"{i}. {name}")
    else:
        print("\nNo names have been picked yet.")

def clearData(allNames: list, availableNames: list, pickHistory: list):
    confirm = input("\nAre you sure you want to clear all names and pick history? (yes/no): ").lower()
    if confirm == 'yes':
        allNames.clear()
        availableNames.clear()
        pickHistory.clear()
        print("Names and pick history cleared!")
    else:
        print("Action cancelled.")

if __name__ == "__main__":
    main()
