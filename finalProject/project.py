import csv
import re
import json

def read_birthstone_data():
    birthstones = {}
    with open("birthstones.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            month = int(row["Month"])
            birthstones[month] = {
                "name": row["Birthstone"],
                "description": row["Description"],
                "famous_people": row["Famous People"].split(","),
                "character_description": row["Character Description"],
            }
    return birthstones

def get_birthstone_character(birthstone_data):
    return birthstone_data.get("character_description", "Unknown")

def display_birthstone_info(stone_name, info, famous_people, character):
    print(f"Your birthstone is {stone_name}!\n")
    print(f"Description: {info}\n")
    print("Famous people with this birthstone include:\n")
    for person in famous_people:
        print(f"- {person}")
    print("Your birthstone character is:\n")
    print(f"- {character}\n")

def save_user_info(name, month, birthstone_data):
    filename = f"{name}.json"
    data = {
        "name": name,
        "month": month,
        "birthstone": birthstone_data,
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Information saved to {filename}\n")

def main():
    try:
        name = input("Enter your name: ")
        if not re.match("^[A-Za-z ]+$", name):
            raise ValueError("Name must contain only letters and spaces.")

        month = int(input("Enter your birth month (1-12): "))
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12.")

        birthstone_data = read_birthstone_data()
        user_birthstone = birthstone_data.get(month, {})

        print(f"Your birthstone is {user_birthstone['name']}.\n")

        choice = input("Would you like to learn more about your birthstone? (yes/no): ").strip().lower()
        if choice == 'yes':
            display_birthstone_info(user_birthstone['name'], user_birthstone['description'], user_birthstone['famous_people'], user_birthstone['character_description'])

        save_choice = input("Would you like to save this information? (yes/no): ").strip().lower()
        if save_choice == 'yes':
            save_user_info(name, month, user_birthstone)

        another = input("Would you like to enter another? (yes/no): ").strip().lower()
        if another == 'yes':
            main()

    except ValueError as e:
        print(e)
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        main()

if __name__ == "__main__":
    main()
