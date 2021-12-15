import pandas as pd
import os
import sys
from tabulate import tabulate
import csv
import re
import time

class Booking:


    def __init__(self):


        self.header = ['Step', 'Description']
        self.table_items = [("Step 1.", "Set Directory"),
                            ("Step 1.", "Name of customer"),
                            ("Step 2.", "Package Description"),
                            ("Step 3.", "Are the contents dangerous"),
                            ("Step 4.", "Weight"),
                            ("Step 5.", "Volume"),
                            ("Step 6", "Required delivery date"),
                            ("Step 7.", "International destination?")]

        self.header_2 = ['Option', 'Selection']
        self.table_2 = [("Urgent 3 day delivery", "Enter 1"),
                        ("Standard Delivery", "Enter 0")]

        self.header_3 = ['Option', 'Selection']
        self.table_3 = [("Ship Internationally", "Enter 1"),
                        ("Do not ship Internationally", "Enter 0")]
        self.table_4 = [("Ship via air", "Enter 1"),
                        ("Do not ship via air", "Enter 0")]

        self.table_5 = [("Exit", "Enter 1"),
                        ("Do not Exit", "Enter 0")]

        self.table_6 = [("Dangerous Content", "Enter 1"),
                        ("No Dangerous Content", "Enter ")]

        self.table_7 = [("Kilograms", "Enter 1"),
                        ("Pounds", "Enter 0")]

        self.table_8 = [("Feet", "Enter 1"),
                        ("Meters", "Enter 0")]

        self.table_9 = [("How many quote would like to create?", "Enter a number!")]

        self.table_10 = [("Enter Required Delivery Date", "Use format mm-dd-yyyy format")]


        self.quote_booking_list = []

    def display_menu(self):

        print(tabulate(self.table_items, headers=self.header, tablefmt="grid"))

    def display_menu_2(self):

        print(tabulate(self.table_2, headers=self.header_2, tablefmt="grid"))

    def display_menu_3(self):

        print(tabulate(self.table_3, headers=self.header_3, tablefmt="grid"))

    def display_menu_4(self):

        print(tabulate(self.table_4, headers=self.header_3, tablefmt="grid"))

    def display_menu_5(self):

        print(tabulate(self.table_5, headers=self.header_3, tablefmt="grid"))

    def display_menu_6(self):

        print(tabulate(self.table_6, headers=self.header_3, tablefmt="grid"))

    def display_menu_7(self):

        print(tabulate(self.table_7, headers=self.header_3, tablefmt="grid"))

    def display_menu_8(self):

        print(tabulate(self.table_8, headers=self.header_3, tablefmt="grid"))

    def display_menu_9(self):

        print(tabulate(self.table_9, headers=self.header_3, tablefmt="grid"))

    def display_menu_10(self):

        print(tabulate(self.table_10, headers=self.header_3, tablefmt="grid"))

    def set_directory(self):

        header_list = ['UID', 'Date', 'Customer Name', 'Air Fare', 'Ground Truck Transport', 'Ocean Freighter Fare']

        selection = input("Enter directory you would like to save booking quote to: ")
        if os.path.exists(selection):
            os.chdir(selection)
            try:
                self.df_booked_quotes = pd.read_csv('booking.csv', index_col=None)
            except:
                FileNotFoundError
                with open('booking.csv', 'wb') as csvfile:
                    csv.writer(csvfile)
                header_df = pd.DataFrame({"QID": [], 'Date': [], 'Customer Name': [], 'Air Fare': [],
                                          'Ocean Freighter Fare': [], 'Ground Truck Transport': []})
                header_df.to_csv('booking.csv', index=False, index_label=None, mode='a')
                self.df_booked_quotes = pd.read_csv('booking.csv', index_col=None)



        if not os.path.exists(selection):
            os.mkdir(selection)
            os.chdir(selection)
            with open('booking.csv', 'wb') as csvfile:
                csv.writer(csvfile)
            header_df = pd.DataFrame({"QID": [], 'Date': [], 'Customer Name': [], 'Air Fare': [],
                                      'Ocean Freighter Fare': [], 'Ground Truck Transport': []})
            header_df.to_csv('booking.csv', index=False, index_label=None, mode='a')
            self.df_booked_quotes = pd.read_csv('booking.csv', index_col=None)

    def generate_unique_id(self):


        qid = int(input('Enter a unique employee ID: '))
        lisut = self.df_booked_quotes['QID'].unique()
        while qid in lisut:
            qid = int(input(f"{qid} is not a unique quote ID. Try Again! Enter a new QID: "))
        self.quote_booking_list.append(qid)

    def get_customer_name(self):

        self.customer_name = input("Please enter your first and last name: ")
        self.quote_booking_list.append(self.customer_name)

    def package_description(self):

        self.package_fragile = ("Is this package fragile y/n: ")

        if self.package_fragile.lower() == 'y':

            self.fragile = True

        if self.package_fragile.lower() == 'n':

            self.fragile = False

    def check_contents(self, dangerous_content):

        while (dangerous_content != '1') and (dangerous_content != '0'):

            self.display_menu_6()
            dangerous_content = input("Try Again! Enter 1 or 0: ")

        if dangerous_content.lower() == '0':
            self.dangerous_contents = False
        if dangerous_content.lower () == '1':
            self.dangerous_contents = True

        return self.dangerous_contents

    def check_weight(self):

        pattern = "\d+\.\d+"
        self.display_menu_7()
        unit = input()
        while (unit !='1') and (unit != '0'):
          unit = input("Please enter 1 or 0 only: ")
        weight = input("How much does your package weigh ?")

        while not re.match(pattern, weight):
            weight = input("Your entry does not match format 0.000 enter again:")

        if unit.lower() == "0":

            print('[----------Converting to Kilograms----------]\n')
            weight = 0.4535 * float(weight)

        return float(weight)

    def get_dimensions(self):

        print("[----------Determine Units----------]\n")
        print("[------Program will convert feet to meters------]\n")

        self.display_menu_8()
        volume_units = input()
        pattern = "\d+\.\d+"

        while volume_units != '1' and volume_units != '0':
            volume_units = input("Enter Again")

        if volume_units.lower() == '1':
            length = input("Please enter length of package in feet(ft) (00.000): ")
            while not re.match(pattern, length):
                length = input("Try Again! Make sure is in feet(ft) (00.000): ")
            width = input("Please enter width of package in feet(ft) (00.000): ")
            while not re.match(pattern, width):
                width = input("Try Again! Make sure is in feet(ft) (00.000): ")
            height = input("Please enter width of package in feet(ft) (00.000): ")
            while not re.match(pattern, height):
                height = input("Try Again! Make sure is in feet(ft) (00.000): ")

            length = 0.3048 * float(length)
            width = 0.3048 * float(width)
            height = 0.3048 * float(height)

        elif volume_units.lower() == '0':
            length = input("Please enter length of package in meters(m): ")
            while not re.match(pattern, length):
                length = input("Try Again! Make sure is format (00.000")
            width = input("Please enter width of package in meters(m): ")
            while not re.match(pattern, width):
                width = input("Try Again! Make sure is format (00.000")
            height = input("Please enter width of package in meters(m): ")
            while not re.match(pattern, height):
                height = input("Try Again! Make sure is format (00.000")

        width_1 = float(width)
        length_1 = float(length)
        height_1 = float(height)

        return length_1, width_1, height_1


    def get_volume(self, length, width, height):

       volume = length * width * height
       volume = round(volume, 3)

       return volume

    def determine_if_shippable(self, volume, weight):

        if volume > 125.000:
            print(f'Can not ship this package volume of {volume} is in excess of 125 cubic meters. ')
            return 1

        if weight > 10.000:
            print(f'Can not ship this package volume of {weight} is in excess of 10 kilograms.')
            return 1

        if (volume > 125.000) and (weight > 10.000):
            print(f'Can not ship due this package having a volume of {volume} and a weight of {weight}.')
            print('[----Resize Package----]')
            return 1
            keyboard_interrupt = input("Enter 1 to continue with new package size or 0 to exit application.")
            if keyboard_interrupt == '1':
             self.display_menu()
             self.menu_prompt()
            else:
                self.system_exit()


        else:
            return True

    def set_weight_boundaries(self, weight):

        if weight >= 5.00:

            self.package_weight_class = 'heavy'
            return 'heavy'
        else:

            self.package_weight_class = 'light'
            return 'light'


    def set_dimension_boundaries(self, volume):

        if (volume >= 75) and (volume <=125):

            self.package_size_class = "large"

        if (volume >=40) and (volume <=74.999):

            self.package_size_class = "medium"

        if (volume >= 0.000 ) and (volume <= 39.999):

            self.package_size_class = "small"

    def determine_urgency(self, urgency):


        if urgency == '1':
           self.urgency = True
        elif urgency == '0':
            self.urgency = False

        return self.urgency

    def determine_international(self):

        self.display_menu_3()
        selection = input()

        while (selection != '1') and (selection != '0'):
          selection = input('Try again! Enter 1 or 0 only: ')

        if selection == '1':

            international = True

        if selection == '0':

            international = False

        return international

    def determine_air_fare(self, weight, volume):

        price_per_kilo = weight * 10
        price_per_volume = volume * 20

        if price_per_kilo > price_per_volume:

            self.air_fare = price_per_kilo

        if price_per_volume > price_per_kilo:

            self.air_fare = price_per_volume

        return self.air_fare

    def determine_truck_fare(self, urgency):

        if urgency == False:

            self.truck_fare = 20.00

        if urgency == True:

            self.truck_fare = 45.00


    def determine_freight_fare(self):

        self.freight_fare = 30.00

    def required_delivery_date(self, date):

        pattern = '\d{2}-\d{2}-\d{4}'
        while not re.match(pattern, date):
            date = input("Try Again! Enter date ins MM-DD-YYYY format: ")

        self.quote_booking_list.append(date)

    def add_to_csv(self):

      try:
        with open('booking.csv', 'a', newline='') as csvfile:
           writer = csv.writer(csvfile)
           writer.writerow(self.quote_booking_list)
      except PermissionError:
          print('Try closing file. Retrying to open file in 5 seconds!')
          time.sleep(10)
          with open('booking.csv', 'a', newline='') as csvfile:
              writer = csv.writer(csvfile)
              writer.writerow(self.quote_booking_list)


            

    def system_exit(self, exit):

       if exit == True:
         return 1
         sys.exit()



    def logistics_planning(self, shippable_package, international_flag, weight, volume, urgency):


        if shippable_package == True:
           if (self.dangerous_contents == False) and (urgency == False):

               self.determine_air_fare(weight, volume)
               self.quote_booking_list.append(self.air_fare)
               return self.air_fare


           if (self.dangerous_contents == False) and (urgency == True):

              self.determine_air_fare(weight, volume)
              self.quote_booking_list.append(self.air_fare)
              return self.air_fare


           if (self.package_weight_class == 'heavy') and (self.package_size_class == 'large'):


               self.determine_truck_fare(urgency)
               self.quote_booking_list.append(self.truck_fare)

           if (self.package_weight_class == 'heavy') and (self.package_size_class == 'medium'):

               self.determine_truck_fare(urgency)
               self.quote_booking_list.append(self.truck_fare)
               return self.truck_fare

           if (self.package_weight_class == 'heavy') and (self.package_size_class == 'small'):

               self.determine_truck_fare(urgency)
               self.quote_booking_list.append(self.truck_fare)
               return self.truck_fare

           if (self.package_weight_class == 'light') and (self.package_size_class == 'large'):

               self.determine_truck_fare(urgency)
               self.quote_booking_list.append(self.truck_fare)
               return self.truck_fare

           if (self.package_weight_class == 'light') and (self.package_size_class == 'medium'):

               self.determine_truck_fare(urgency)
               self.quote_booking_list.append(self.truck_fare)
               return self.truck_fare

           if (self.package_weight_class == 'light') and (self.package_size_class == 'small'):

               self.determine_truck_fare(urgency)
               self.quote_booking_list.append(self.truck_fare)
               return self.truck_fare

           if (self.dangerous_contents == True) and (international_flag == False):

               self.determine_truck_fare(urgency)
               self.quote_booking_list.append(self.truck_fare)
               return self.truck_fare

           if (self.dangerous_contents == True) and (international_flag == True):

                self.determine_freight_fare()
                self.quote_booking_list.append(self.freight_fare)
                return self.freight_fare

           if (self.package_weight_class == 'heavy') and (self.package_size_class == 'large') \
               and (international_flag == True):

               self.determine_freight_fare()
               self.quote_booking_list.append(self.freight_fare)
               return self.freight_fare

           if (self.package_weight_class == 'heavy') and (self.package_size_class == 'medium') \
               and (international_flag == True):

               self.determine_freight_fare()
               self.quote_booking_list.append(self.freight_fare)
               return self.freight_fare

           if (self.package_weight_class == 'heavy') and (self.package_size_class == 'small') \
               and (international_flag == True):

               self.determine_freight_fare()
               self.quote_booking_list.append(self.freight_fare)
               return self.freight_fare

           if (self.package_weight_class == 'light') and (self.package_size_class == 'large') \
               and (international_flag == True):

               self.determine_freight_fare()
               self.quote_booking_list.append(self.freight_fare)
               return self.freight_fare

           if (self.package_weight_class == 'light') and (self.package_size_class == 'medium') \
               and (international_flag == True):

               self.determine_freight_fare()
               self.quote_booking_list.append(self.freight_fare)
               return self.freight_fare

           if (self.package_weight_class == 'light') and (self.package_size_class == 'small') \
               and (international_flag == True):

               self.determine_freight_fare()
               self.quote_booking_list.append(self.freight_fare)
               return self.freight_fare




