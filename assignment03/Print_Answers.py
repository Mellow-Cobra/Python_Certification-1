import csv
import os
i=0
question = []
answer = []
os.chdir('C:\\Users\\MMR3\\Documents\\UW\\Lesson_2')

with open('answers.csv', 'r') as csv_file1:
    reader = csv.reader(csv_file1)
    with open('questions.csv', 'r') as question_file:
        reader1 = csv.reader(question_file)
        for line in reader1:
            question.append(line[2])
        for line in reader:
            print(question[i] + line[2])
            i+=1
