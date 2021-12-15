import os
import csv

headings = ("PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked")

os.chdir("C:\\Users\\MMR3\\Documents\\UW\\")

if os.path.isfile("Titanic.csv") is True:
    print("exists")

else:

    print("does not exist")


with open("titanic.csv") as csv_file:
     data = csv.reader(csv_file)

     for row in data:

        tuple(row)


