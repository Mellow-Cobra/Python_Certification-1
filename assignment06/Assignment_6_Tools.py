import pandas as pd
import os
import time
from tabulate import tabulate
import csv
import sys
from datetime import datetime, timedelta


class Menu:

    def __init__(self):

        self.employee_data_directory = input('Enter file path to csv: ')
        os.chdir(self.employee_data_directory)
        self.employee_data_file = input('Enter employee data file name (include extension): ')

        self.header = ['Select', 'Description']
        self.table_items = [{"Amend", "Amend Employee Data in data file"},
                            {"Add", "Add new Employee Data to data file"},
                            {"View", "View all entries in CSV file"},
                            {"Current", "View Current Employees"},
                            {"CSV", "Make CSV file"},
                            {"Review", "Schedule for Review"},
                            {"Former", "View Former Employees"},
                            {"Exit", "Exit this application"}]

        self.amend_table_items = [{"E", "Set End Date"},
                                  {"J", "Change Job Title"},
                                  {"S", "Change Salary"}]
        self.dataframe = pd.DataFrame({"EID": [], "First Name": [], "Last Name": [], "Street": [], "City": [],
                                       "State": [], "Zip Code": [], "SSN": [], "DOB": [], "Job Title": [],
                                       "Salary": [], "Start Date": [], "End Date": []})

        try:
            self.employee_data = pd.read_csv(self.employee_data_file)
        except FileNotFoundError:
            print('File does not Exist! Program Will Create File!\n')
            self.dataframe.to_csv(self.employee_data_file)

        self.employee_id_data = []
        self.first_name_data = []
        self.last_name_data = []
        self.street_name_data = []
        self.city_name_data = []
        self.state_name_data = []
        self.zip_code_data = []
        self.ssn_id_data = []
        self.dob_id_data = []
        self.job_title_data = []
        self.salary_data = []
        self.start_date_data = []
        self.end_date_data = []

    @staticmethod
    def exit_function():

        sys.exit()

    def add_employees_to_csv(self):

        employees_to_add = int(input('How many employees would you like to add? '))

        for i in range(0, employees_to_add):
            eid = int(input('Enter a unique employee ID: '))
            print(self.employee_data['EID'].unique())
            lisut = self.employee_data['EID'].unique()
            while eid in lisut:
                eid = int(input(str(eid) + " is not unique, enter EID again: "))
            self.employee_id_data.append(eid)

            self.first_name_data.append(input('Enter their first name:'))
            self.last_name_data.append(input('Enter their last name:'))
            self.street_name_data.append(input('Enter Street Name:'))
            self.city_name_data.append(input('Enter city name:'))
            self.state_name_data.append(input('Enter state name:'))
            self.zip_code_data.append(input('Enter zip code:'))
            self.ssn_id_data.append(input('Enter their SSN:'))
            dob_id = input('Enter their DOB (mm-dd-yyyy):')
            while self.validate_date(dob_id) is False:
                dob_id = input('Please correct dob date to match format (mm-dd-yyyy):')
            self.dob_id_data.append(dob_id)
            self.job_title_data.append(input('Enter their job title:'))
            self.salary_data.append(input('Enter their salary:'))
            start_date = input('Enter the employees start date: ')
            end_date = input('Enter the employees end date: ')
            result = self.check_start_and_end_dates(start_date, end_date)
            while result == False:
                start_date = input('Enter the employees start date: (mm-dd-yyyy): ')
                end_date = input('Enter the employees end date:(mm-dd-yyyy): ')
                result = self.check_start_and_end_dates(start_date, end_date)
            self.start_date_data.append(start_date)
            self.end_date_data.append(end_date)

            df = pd.DataFrame({'EID': [self.employee_id_data[i]], 'First Name': [self.first_name_data[i]],
                               "Last Name": [self.last_name_data[i]], 'Street': [self.street_name_data[i]],
                               'City': [self.city_name_data[i]], 'State': [self.state_name_data[i]],
                               'Zip Code': [self.zip_code_data[i]], 'SSN': [self.ssn_id_data[i]],
                               'DOB': [self.dob_id_data[i]], 'Job Title': [self.job_title_data[i]],
                               'Salary': [self.salary_data[i]], 'Start Date': [self.start_date_data[i]],
                               'End Date': [self.end_date_data[i]]})

            df.to_csv(self.employee_data_file, mode='a', index=False, header=False)

    def amend_employee(self):

        eid = input('Enter Employee ID that you would like to amend: ')
        file_to_amend = pd.read_csv(self.employee_data_file, index_col=False)
        self.display_list(self.employee_data_file)

        column_to_amend = input('Enter column that you would like to amend: ')
        amended_data_value = input('Enter the value you would this to change to: ')
        file_to_amend.loc[file_to_amend['EID'] == eid, column_to_amend] = amended_data_value
        file_to_amend.to_csv(self.employee_data_file, mode='w', index=False)

    @staticmethod
    def validate_date(self, date):

        try:
            datetime.strptime(date, '%m-%d-%Y')
            return True
        except ValueError:
            return False

    def check_start_and_end_dates(self, start_date, end_date):

        if self.validate_date(start_date) is False:
            print('Please correct start date to match format (mm-dd-yyyy):')
            return False
        if self.validate_date(end_date) is False:
            print('Please correct End date to match format (mm-dd-yyyy):')
            return False

        result = start_date < end_date
        if result is False:
            print('Start date cannot be greater than End Date\n')

        return result


    def display_list(self, list):

        data_to_display = pd.read_csv(list)

        print(tabulate(data_to_display, headers=data_to_display.head(0), tablefmt="grid"))

    def display_menu(self):

        print(tabulate(self.table_items, headers=self.header, tablefmt="grid"))
        self.selection = input("Select an item from above table: ")

    def find_current_employees(self):

        df = pd.read_csv(self.employee_data_file)
        current_employees = (df[pd.to_datetime(df['End Date']) > datetime.now()])
        print("Printing list of Current employees")
        print(tabulate(current_employees.sort_values('EID'), headers=current_employees.head(0), tablefmt="grid"))

    def find_former_employees(self):

        current_time = datetime.now()
        print(current_time.month)
        print(current_time.year)

        df = pd.read_csv(self.employee_data_file)
        former_employees = (df[pd.to_datetime(df['End Date']) < datetime.now()])

        for i, row in former_employees.iterrows():

            end_time = pd.to_datetime(row['End Date'])
            year_difference = current_time.year - end_time.year
            month_difference = current_time.month - end_time.month
            months_between_dates = (year_difference * 12) + month_difference
            if months_between_dates > 1:
                former_employees = former_employees.drop(index=i)

        print("Printing list of former employees")
        print(tabulate(former_employees.sort_values('EID'), headers=former_employees.head(0), tablefmt="grid"))

    def annual_review(self):

        current_date = datetime.now()
        df = pd.read_csv(self.employee_data_file)
        current_employees = (df[pd.to_datetime(df['End Date']) > datetime.now()])

        for i, row in current_employees.iterrows():
            start_date = pd.to_datetime(row['Start Date'])
            n_years = int((current_date - start_date) / timedelta(365))

            next_review_date = self.add_years_to_date(start_date, n_years+1)

            # Review should be in next 90 days == 3 months
            if next_review_date - current_date <= timedelta(90):
                print(row['First Name'] +" Your next review cycle is in 3 months " + str(next_review_date))

    def create_new_csv(self):

        csv_file_name = input("What name would you like to give your csv file? ")

        csv_file_location = input("Where would you like to store your CSV? ")

        if os.path.exists(csv_file_location):
            os.chdir(csv_file_location)
            self.dataframe.to_csv(csv_file_name, index=False)
        if not os.path.exists(csv_file_location):
            os.mkdir(csv_file_location)
            os.chdir(csv_file_location)
            self.dataframe.to_csv(csv_file_name, index=False)

        self.employee_data_file = csv_file_name

    def add_years_to_date(self, date, n_years):
        future_date = date + pd.DateOffset(years=n_years)
        return future_date

    def add_months_to_date(self, date, n_months):
        future_date = date + pd.DateOffset(months=n_months)
        return future_date

    def menu_selections(self):

        while True:

            if self.selection.lower() == 'amend':
                self.amend_employee()

            if self.selection.lower() == 'add':
                self.add_employees_to_csv()

            if self.selection.lower() == 'csv':

                self.create_new_csv()


            if self.selection.lower() == "former":
                self.find_former_employees()

            if self.selection.lower() == 'review':
                self.annual_review()

            if self.selection.lower() == "current":
                self.find_current_employees()

            if self.selection.lower() == 'view':
                self.display_list(self.employee_data_file)

            if self.selection.lower() == 'exit':
                self.exit_function()

            self.display_menu()
            self.menu_selections()
