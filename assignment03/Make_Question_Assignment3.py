import os
import csv
import random

os.chdir('C:\\Users\\MMR3\\Documents\\UW\\Lesson_2')


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
