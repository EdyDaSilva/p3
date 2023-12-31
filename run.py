import csv
import re


# create csv file
# with open("sheep_data.csv", "w+") as file:
#     myFile = csv.writer(file)
#     myFile.writerow(["ID Tag", "DOB", "Sex", "Other Info"])


def append_to_csv():
    # Open the CSV file in append mode
    with open("sheep_data.csv", "a", newline="") as file:
        myFile = csv.writer(file)

        # id_tag = int(input("Enter ID Tag: "))
        # Prompt the user for information
        while True:
            id_tag = input("Enter ID Tag: ")
            
            if id_tag.isdigit():
                id_tag = int(id_tag)
                break
            else:
                print("Please enter a valid number for ID Tag.")
        
        while True:
            dob = input("Enter DOB (YYYY-MM-DD): ")
            # Use regular expression to check if input matches the date format YYYY-MM-DD
            if re.match(r'^\d{4}-\d{2}-\d{2}$', dob):
                break
            else:
                print("Please enter a valid date in the format YYYY-MM-DD.")
        
        # dob = input("Enter DOB: ")
        # sex = input("Enter Sex: ")
        while True:
            sex = input("Enter Sex (M/F): ").upper()
            if sex.upper() in ['M', 'F']:
                break
            else:
                print("Please enter 'M' for male or 'F' for female.")
        other_info = input("Enter Other Info: ")
        if not other_info:
            other_info = "N/A"
        
        # Write the user's input to the CSV file
        myFile.writerow([id_tag, dob, sex, other_info])


# append_to_csv()


'''
function to update other information field
'''
def update():
    f = open("sheep_data.csv", 'r', newline='\n')
    tag_to_find = input("Enter tag N to find: ")
    tag_found = 0
    r = csv.reader(f)
    tag_updated = []
    for rec in r:
        if rec[0] == tag_to_find:
            print("Tag to update is found: ", rec)
            rec[3] = input("Enter Other Info: ")
            if not rec[3]:
                rec[3] = "N/A"
            print("Updated Other Info: ", rec)
            tag_found = 1
        tag_updated.append(rec)

    if tag_found == 0:
        print("Tag does not exist")
        f.close()

    else:
        f = open("sheep_data.csv", 'w', newline='')
        w = csv.writer(f)
        w.writerows(tag_updated)
        f.close()
            

# update()

# Usage
# if __name__ == "__main__":
#     filename = "sheep_data.csv"
#     update(filename)


def choose_action():
    while True:
        choice = input("Enter 'A' to add new object or 'B' to update or 'Q' to quit: ").upper()
        if choice == "A":
            append_to_csv()
        elif choice == "B":
            update()
        elif choice == "Q":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 'a', 'b', or 'q'")


choose_action()
