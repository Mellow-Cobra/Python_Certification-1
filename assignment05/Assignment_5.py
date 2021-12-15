from operator import itemgetter
import time
import sys


donor_data = [("William Gates, III", [100.0, 120.10]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 343.87, 411.32]),
            ("Mark Zuckerberg", [1660.23, 4320.87, 10432.0]),
            ]


def get_name_of_user():

    name_of_user = input('What is your name ? ')

    return name_of_user

def add_get_donors():

 name_of_donor = [donor_name[0] for donor_name in donor_data]
 type_of_name = input('Enter List to see donors else enter a name: ')

 while ( type_of_name.lower() == 'list'):

    type_of_name = input('Enter list to see donors else enter a name: ')
    if (type_of_name.lower() == 'list'):
        print(name_of_donor)
 if (type_of_name not in name_of_donor):
    donation = input('How much would you like to donate ' + type_of_name + " ? ")
    donor_data.append((type_of_name, [donation]))
    print(donor_data)
 elif (type_of_name in name_of_donor):
    donation_amount = int(input('Enter the amount this person had donated: '))
    donated = [donation[1] for donation in donor_data]
    print(donated)
 print('Thank you %s for your generous donation.' % (type_of_name))




def create_report():

    total = []
    average_gift = []
    name_of_donor = [donor_name[0] for donor_name in donor_data]
    donations = [donation[1] for donation in donor_data]
    for i in range(len(donations)):
        total.append(sum(donations[i]))
        average_gift.append(sum(donations[i]) / len(donations))
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('--------------------------------------------------------------------')
    for i in range(len(name_of_donor)):
     print(name_of_donor[i] + "              $" + str(total[i]) + " " + "$ " + str(average_gift[i]))


def exit_program():

    print("Quitting Program in 5 seconds!")
    time.sleep(5)
    sys.exit()


def main():

    user_name = get_name_of_user()
    print('Hello ' + user_name)
    while True:
     selection = input('Enter for S to Send a Thank you \n' +
                      ' Enter R to create report or Q to quit! \n')
     if (selection.lower() == 's'):
        add_get_donors()
     elif (selection.lower() == 'r'):
        create_report()
     elif (selection.lower() == 'q'):
        exit_program()


if __name__ == "__main__":
    main()
