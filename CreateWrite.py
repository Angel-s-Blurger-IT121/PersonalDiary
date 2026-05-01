#Create
def create_file():
    try:
        file = open("Diary.txt", "x")
        print("File 'Diary.txt' created successfully!!!")
        file.close()
    except FileExistsError:
        print("File 'Diary.txt' already exists!")

#Append
def append_entry():
    try:
        date = input("Enter date: ")
        entry = input("Write your diary entry: ")

        file = open("Diary.txt", "a")
        file.write(f"[{date}] {entry}\n")
        file.close()

        print("Entry added!")

    except Exception as e:
        print("Error:", e)

#Read
def read_entries():
    try:
        file = open("Diary.txt", "r")
        lines = file.readlines()

        print("\n--- Diary Entries ---")
        for line in lines:
            print(line.strip())

        print(f"\nTotal entries: {len(lines)}")
        file.close()

    except FileNotFoundError:
        print("Diary entry not found.")
    except Exception as e:
        print("Error:", e)

#Update
def update_entry():
    try:
        date_to_update = input("Enter date to update: ")
        file = open("Diary.txt", "r")
        lines = file.readlines()
        file.close()
        file = open("Diary.txt", "w")

        found = False
        for line in lines:
            if date_to_update in line:
                new_entry = input("Enter new entry: ")
                file.write(f"[{date_to_update}] {new_entry}\n")
                found = True
            else:
                file.write(line)

        file.close()

        if found:
            print("Entry updated!")
        else:
            print("Date not found.")

    except FileNotFoundError:
        print("Diary entry not found.")
    except Exception as e:
        print("Error:", e)

#Search
def search_entry():
    try:
        keyword = input("Enter keyword/date to search: ")
        file = open("Diary.txt", "r")
        found = False

        for line in file:
            if keyword.lower() in line.lower():
                print("Found:", line.strip())
                found = True

        if not found:
            print("No entry found.")
        file.close()

    except FileNotFoundError:
        print("Diary entry not found.")
    except Exception as e:
        print("Error:", e)

#Delete
def delete_entry():
    try:
        date_to_delete = input("Enter date to delete: ")

        file = open("Diary.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("Diary.txt", "w")

        found = False
        for line in lines:
            if date_to_delete not in line:
                file.write(line)
            else:
                found = True

        file.close()

        if found:
            print("Entry deleted!")
        else:
            print("Date not found.")

    except FileNotFoundError:
        print("Diary entry not found.")
    except Exception as e:
        print("Error:", e)


#Main Menu
create_file()


while True:
    print("\n==== PERSONAL DIARY MENU ====")
    print("1. Add Entry")
    print("2. Read Entries")
    print("3. Update Entry")
    print("4. Search Entry")
    print("5. Delete Entry")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        append_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        update_entry()
    elif choice == "4":
        search_entry()
    elif choice == "5":
        delete_entry()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please choose again.")