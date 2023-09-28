import csv

with open("sheep_data.csv", "w+") as file:
    myFile = csv.writer(file)
    myFile.writerow(["ID Tag", "DOB", "Sex", "Other Info"])