import datetime


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<Welcome {} {}!>".format(self.first_name, self.last_name)

    def get_dob(self):
        dob = input("Enter your DOB in the format YYYY-MM-DD\n")
        return dob

    # def convert_str_date(self, date_str):
    #     year, month, day = map(int, date_str.split('-'))
    #     date = datetime.date(year, month, day)
    #     return date

    def convert_into_date(self, date_str):
        while True:
            try:
                year, month, day = map(int, date_str.split('-'))
                date = datetime.date(year, month, day)
            except ValueError:
                return 0
            else:
                return date

    def check_dob(self, dob):
        delta_days = (datetime.date.today() - dob).days
        delta_years = delta_days / 365
        return delta_years

    def choose_date_ongoing(self):
        date_ongoing = input("Choose the date of your flight (YYYY-MM-DD)\n")
        # year, month, day = map(int, date_entry.split('-'))
        # date_ongoing = datetime.date(year, month, day)
        return date_ongoing

    def choose_date_return(self):
        date_entry = input("Choose the date of your flight (YYYY-MM-DD)\n")
        year, month, day = map(int, date_entry.split('-'))
        date_return = datetime.date(year, month, day)
        return date_return

    def check_dates(self, date_ongoing, date_return):
        delta = date_return - date_ongoing
        if delta.days <= 0:
            print("Your return needs to be further in time")






