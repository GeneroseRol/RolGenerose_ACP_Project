import random
import csv
import os

def main():
    print("="*40)
    print("   WELCOME TO THE RANDOM NAME PICKER!    ")
    print("="*40)

    csv_file = input("Enter the name of the CSV file to use: ").strip()
    if not csv_file.endswith('.csv'):
        csv_file += '.csv'

    all_names, available_names = load_names_from_csv(csv_file)
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
        print("8. Reset Names")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            all_names, available_names = add_names(all_names, available_names, csv_file)
        elif choice == "2":
            display_all_names(all_names)
        elif choice == "3":
            display_available_names(available_names)
        elif choice == "4":
            pick_random(available_names, pick_history)
        elif choice == "5":
            pick_multiple(available_names, pick_history)
        elif choice == "6":
            display_pick_history(pick_history)
        elif choice == "7":
            clear_data(all_names, available_names, pick_history)
        elif choice == "8":
            reset_names(all_names, available_names, pick_history)
        elif choice == "9":
            print("Thank you and Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def load_names_from_csv(csv_file):
    if not os.path.exists(csv_file):
        return [], []

    all_names = []
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                all_names.append(row[0])
    return all_names, all_names[:]

def add_names(all_names: list, available_names: list, csv_file: str) -> list:
    print("\nEnter names (type 'done' to stop):")
    while True:
        name = input("> ").strip()
        if name.lower() == 'done':
            break
        elif name and name not in all_names:
            all_names.append(name)
            available_names.append(name)
            save_name_to_csv(csv_file, name)
        elif not name:
            print("Name cannot be empty. Please enter a name.")
        else:
            print(f"{name} is already in the list.")
    return all_names, available_names

def save_name_to_csv(csv_file, name):
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name])

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

def pick_random(available_names: list, pick_history: list) -> None:
    if available_names:
        name = random.choice(available_names)
        available_names.remove(name)
        pick_history.append(name)
        print(f"\nRandomly picked: {name}")
    else:
        print("\nNo names available to pick from.")

def pick_multiple(available_names: list, pick_history: list) -> None:
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

def display_pick_history(pick_history: list):
    if pick_history:
        print("\nPick History:")
        for i, name in enumerate(pick_history, 1):
            print(f"{i}. {name}")
    else:
        print("\nNo names have been picked yet.")

def reset_names(all_names: list, available_names: list, pick_history: list):
    restart = input("\nWould you like to start with all the names again? (yes/no): ").lower()
    if restart == 'yes':
        available_names[:] = all_names
        pick_history.clear()
        print("Names list and pick history have been reset.")
    else:
        print("Exit.")

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
