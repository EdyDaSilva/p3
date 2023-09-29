import csv

# create csv file
# with open("sheep_data.csv", "w+") as file:
#     myFile = csv.writer(file)
#     myFile.writerow(["ID Tag", "DOB", "Sex", "Other Info"])

def append_to_csv(filename):
    # Open the CSV file in append mode
    with open("sheep_data.csv", "a", newline="") as file:
        myFile = csv.writer(file)
        
        # Prompt the user for information
        while True:
            id_tag = input("Enter ID Tag: ")
            
            if id_tag.isdigit():
                id_tag = int(id_tag)
                break
            else:
                print("Please enter a valid number for ID Tag.")
        # id_tag = int(input("Enter ID Tag: "))
        dob = input("Enter DOB: ")
        sex = input("Enter Sex: ")
        other_info = input("Enter Other Info: ")
        
        # Write the user's input to the CSV file
        myFile.writerow([id_tag, dob, sex, other_info])

# Usage
if __name__ == "__main__":
    filename = "sheep_data.csv"
    append_to_csv(filename)