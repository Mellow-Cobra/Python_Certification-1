answer_list = []
question_tuple = ("What is your name ? ", "What is your conference ID ? ", "What is your email address ? ", "State any food preferences: ")
sessions_tuple = ("Python for beginners", "Database development with Python", "Python for data science", "Advanced Python for application developers")
dialog_tuple_1 = ("Your name is ", "Your conference ID is: ", "You email address is: ", "Your food prefence is: " )
attendance_list = []
sessions_list = []

print("########################################")
print("| Welcome to Seattle Python Conference |")


for i in range(len(question_tuple)):

    answer_list.append(input(question_tuple[i]))


print("Select which of the following sessions you wish to attend – enter y or n")
for i in range(len(sessions_tuple)):
 attendance_list.append(input(sessions_tuple[i]))

for i in range(len(attendance_list)):

    if (attendance_list[i] == 'y'):

        sessions_list.append(sessions_tuple[i])


for i in range(len(dialog_tuple_1)):

    print(dialog_tuple_1[i] + answer_list[i] +"\n")

print("You will be attending sessions: ")

for i in range(len(sessions_list)):

    print(sessions_list[i] + " ")