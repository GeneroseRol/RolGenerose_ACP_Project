import random

def main():
    print("="*40)
    print("    WELCOME TO THE RANDOM NAME PICKER!    ")
    print("="*40)
    all_names = []
    available_names = []
    pick_history = []

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
            all_names, available_names = add_names(all_names, available_names)
        elif choice == "2":
            display_all_names(all_names)
        elif choice == "3":
            display_available_names(available_names)
        elif choice == "4":
            pick_random(available_names, pick_history, all_names)
        elif choice == "5":
            pick_multiple(available_names, pick_history, all_names)
        elif choice == "6":
            display_pick_history(pick_history)
        elif choice == "7":
            clear_data(all_names, available_names, pick_history)
        elif choice == "8":
            print("Thank you and Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_names(all_names: list, available_names: list) -> tuple:
    print("\nEnter names (type 'done' to stop):")
    while True:
        name = input("> ").strip()
        if name.lower() == 'done':
            break
        elif name and name not in all_names:
            all_names.append(name)
            available_names.append(name)
        elif not name:
            print("Name cannot be empty. Please enter a name.")
        else:
            print(f"{name} is already in the list.")
    return all_names, available_names

def display_all_names(all_names: list):
    if all_names:
        print("\nAll names entered:")
        for i, name in enumerate(all_names, 1):
            print(f"{i}. {name}")
    else:
        print("\nNo names available. Enter names first.")

def display_available_names(available_names: list):
    if available_names:
        print("\nCurrent available names (not picked yet):")
        for i, name in enumerate(available_names, 1):
            print(f"{i}. {name}")
    else:
        print("\nNo available names. Add names first.")

def pick_random(available_names: list, pick_history: list, all_names: list) -> None:
    if available_names:
        name = random.choice(available_names)
        available_names.remove(name)
        pick_history.append(name)
        print(f"\nRandomly picked: {name}")
    else:
        print("\nNo names available to pick from.")
        restart = input("Would you like to start with all the names again? (yes/no): ").lower()
        if restart == 'yes':
            available_names[:] = all_names
            pick_history.clear()
            print("Names list and pick history have been reset.")
        else:
            print("Exit.")

def pick_multiple(available_names: list, pick_history: list, all_names: list) -> None:
    if available_names:
        while True:
            try:
                num_to_pick = int(input(f"\nEnter the number of names to pick (1-{len(available_names)}): "))
                if num_to_pick < 1 or num_to_pick > len(available_names):
                    print("\nInvalid number. Please pick between 1 and the number of names available.")
                else:
                    picked_names = random.sample(available_names, num_to_pick)
                    for picked in picked_names:
                        available_names.remove(picked)
                    pick_history.extend(picked_names)
                    print(f"\nRandomly picked names: {', '.join(picked_names)}")
                    break
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
    else:
        print("\nNo names available.")
        restart = input("Would you like to start with all the names again? (yes/no): ").lower()
        if restart == 'yes':
            available_names[:] = all_names
            pick_history.clear()
            print("Names list and pick history have been reset.")
        else:
            print("Exit.")

def display_pick_history(pick_history: list):
    if pick_history:
        print("\nPick History:")
        for i, name in enumerate(pick_history, 1):
            print(f"{i}. {name}")
    else:
        print("\nNo names have been picked yet.")

def clear_data(all_names: list, available_names: list, pick_history: list):
    confirm = input("\nAre you sure you want to clear all names and pick history? (yes/no): ").lower()
    if confirm == 'yes':
        all_names.clear()
        available_names.clear()
        pick_history.clear()
        print("Names and pick history cleared!")
    else:
        print("Exit.")

if __name__ == "__main__":
    main()
