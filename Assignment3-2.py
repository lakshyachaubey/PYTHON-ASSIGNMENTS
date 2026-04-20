import os

FILE_NAME = "my_tasks.txt"


def setup_file():
    if not os.path.isfile(FILE_NAME):
        open(FILE_NAME, "w").close()


def add():
    tid = input("Task ID: ")
    desc = input("Description: ")
    stat = input("Status (P/C): ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{tid},{desc},{stat}\n")

    print("Task saved!\n")


def show():
    try:
        with open(FILE_NAME, "r") as f:
            data = f.readlines()

        if len(data) == 0:
            print("No records found.\n")
            return

        print("\n--- All Tasks ---")
        for line in data:
            tid, desc, stat = line.strip().split(",")
            print(f"[{tid}] {desc} --> {stat}")

        print()

    except FileNotFoundError:
        print("File missing.\n")


def edit():
    tid = input("Enter ID to modify: ")
    updated = False

    with open(FILE_NAME, "r") as f:
        data = f.readlines()

    with open(FILE_NAME, "w") as f:
        for line in data:
            old_id, desc, stat = line.strip().split(",")

            if old_id == tid:
                updated = True
                new_desc = input("New desc (leave blank to keep same): ")
                new_stat = input("New status (leave blank to keep same): ")

                if new_desc:
                    desc = new_desc
                if new_stat:
                    stat = new_stat

            f.write(f"{old_id},{desc},{stat}\n")

    print("Updated!\n" if updated else "ID not found.\n")


def remove():
    tid = input("Enter ID to remove: ")
    found = False

    with open(FILE_NAME, "r") as f:
        data = f.readlines()

    with open(FILE_NAME, "w") as f:
        for line in data:
            old_id, desc, stat = line.strip().split(",")

            if old_id == tid:
                found = True
                continue

            f.write(line)

    print("Deleted!\n" if found else "ID not found.\n")


def find():
    key = input("Search keyword: ").lower()
    found = False

    with open(FILE_NAME, "r") as f:
        for line in f:
            tid, desc, stat = line.strip().split(",")

            if key in tid.lower() or key in desc.lower():
                found = True
                print(f"{tid} | {desc} | {stat}")

    if not found:
        print("Nothing found.")
    print()


def main():
    setup_file()

    while True:
        print("==== TASK MANAGER ====")
        print("1.Add  2.View  3.Edit  4.Delete  5.Search  0.Exit")

        ch = input("Choice: ")

        if ch == "1":
            add()
        elif ch == "2":
            show()
        elif ch == "3":
            edit()
        elif ch == "4":
            remove()
        elif ch == "5":
            find()
        elif ch == "0":
            print("Bye!")
            break
        else:
            print("Wrong input\n")


if __name__ == "__main__":
    main()