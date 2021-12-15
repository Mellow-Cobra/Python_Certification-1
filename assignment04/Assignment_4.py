import csv
import os
import re
import random

i=0
question = []
answer = []
corrected_question = []
os.chdir('C:\\Users\\MMR3\\Documents\\UW\\Assignment 4')
characters = 0

#############################
# Create Questions
#############################

os.chdir('C:\\Users\\MMR3\\Documents\\UW\\Assignment 4')


amount_of_questions = int(input('How many questions do you want to add ? '))


if not os.path.exists('questions.csv'):
    sequence_number = 0
    question_id = []
    for i in range(amount_of_questions):
        question_id.append(i)
    with open('questions.csv', 'w') as questions:
        for i in range(amount_of_questions):
            store_question = input('Please input a question: ')
            questions.write(str(question_id[i] + random.randint(0, 10000)) + "," + str(sequence_number) + "," + store_question + "\n")
            sequence_number += 1
########################
# Create Answers
########################

print("########################################")
print("| Welcome to Seattle Python Conference |")
name = input("What is you name ? ")

os.chdir('C:\\Users\\MMR3\\Documents\\UW\\Assignment 4')
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

##################
# Validate Answers
##################


with open('answers.csv', 'r') as csv_file1:
    reader = csv.reader(csv_file1)
    with open('questions.csv', 'r') as question_file:
        reader1 = csv.reader(question_file)
        for line in reader1:
            question.append(line[2])
        for line in reader:
            print(question[i] + "\n")
            correct_answer = input("Is the above question correct ? ")
            for i in range(len(question)):
                characters += 1
            print(characters)
            if ((correct_answer.lower() == 'correct')):
                if (characters >= 10) and (characters <= 30):
                    print('you are happy')
                else:
                    make_correction = input("Do you wish to make an adjustment to your question ? ")
                    if (make_correction.lower() == 'y'):
                        corrected_question.append()
                        delete_question = input('Do you wish to delete this question y/n ?')
                        if (delete_question.lower() == 'y'):
                            confirm_delete =  input('Are you certain you want to delete this question y/n ?')
                            if (confirm_delete.lower() == 'y'):
                                print('delete')
                            elif (confirm_delete.lower() == 'n'):
                                print('will not delete')



        i += 1
#################################
#   Part 2
#################################


