
import random


class Plane:

    def __init__(self, airline="N'gouzo Airline"):
        self.airline = airline
        self.customers = []

    def __repr__(self):
        return "<Welcome to {}>".format(self.airline)

    def make_seats(self):
        seats_num = []
        for n in range(1, 30):
            for letter in list('ABCDEF'):
                seats_num.append(str(n) + letter)
        random.shuffle(seats_num)
        return seats_num

    # def pick_seat(self, lst_seats):
    #     seat = lst_seats.pop()
    #     return seat


    # def get_first_name(self):
    #     first_name = input("Enter your first name\n")
    #     return first_name

    # def get_last_name(self):
    #     last_name = input("Enter your last name\n")
    #     return last_name

    # def get_dob(self):
    #     dob = input("Enter your DOB in the format YYYY-MM-DD\n")
    #     return dob
    #
    # def convert_str_date(self, date_str):
    #     year, month, day = map(int, date_str.split('-'))
    #     date = datetime.date(year, month, day)
    #     return date
    #
    # def check_dob(self, dob):
    #     delta_days = (datetime.date.today() - dob).days
    #     delta_years = delta_days / 365
    #     return delta_years

    # def create_new_customer(self, first_name, last_name, dob):
    #     customer = Customer(first_name, last_name, dob)
    #     self.customers.append(customer)
    #     return self.customers

    # def save_to_file(self, fitst_name, last_name, dob):
    #     with open("Passengers.txt", 'w') as f:
    #         for customer in self.customers:
    #             f.write("{}, {}, {}\n".format(fitst_name, last_name, str(dob)))










