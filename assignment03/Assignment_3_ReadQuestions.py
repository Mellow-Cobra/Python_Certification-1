import os
import csv


print("########################################")
print("| Welcome to Seattle Python Conference |")
name = input("What is you name ? ")

os.chdir('C:\\Users\\MMR3\\Documents\\UW\\Lesson_2')
rowcount = 0
i = 0
sequence_number = []
questions = []
qid_from_csv = {}
dict_from_csv = {}
answer = []

for row in open("questions.csv"):
  rowcount+= 1

with open('questions.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for lines in csv_reader:
     dict_from_csv[lines[1]] = lines[2]
     qid_from_csv[lines[1]] = lines[0]
with open('answers.csv', 'a') as file:
 for key in sorted(dict_from_csv):
    answer.append(input(dict_from_csv[key]))
 for key in sorted(qid_from_csv):
     file.write(qid_from_csv[key]+","+name+","+answer[i]+"\n")
     i+=1

