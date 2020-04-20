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

    def convert_into_date(self, date_str):
        while True:
            try:
                year, month, day = map(int, date_str.split('-'))
                date = datetime.date(year, month, day)
            except ValueError:
                return 0
            else:
                return date

    def check_age(self, dob):
        delta_days = (datetime.date.today() - dob).days
        delta_years = delta_days / 365
        return delta_years

    def choose_one_way_or_return(self):
        while True:
            try:
                num_flight = int(input("Choose 1 for one way or 2 for a return ticket\n"))
            except ValueError:
                continue
            else:
                return num_flight

    def choose_ongoing_date(self):
        date_ongoing = input("Choose the date of your flight (YYYY-MM-DD)\n")
        return date_ongoing

    # WE HAVE STOPPED HERE. WE NEED TO CHECK THAT ONGOING TICKET IS COUPLE OF HOURS AWAY.
    def verify_ongoing_date(self, ongoing_date):
        # delta_h = (ongoing_date - datetime.date.today()).hour
        pass


    def choose_random_manual_seat(self):
        while True:
            try:
                answer = int(input("Enter 0 to get a random seat number\n"
                               "or 1 to choose your own seat\n"))
            except ValueError:
                print("You can only enter 0 or 1\n")
                continue
            if answer == 0 or answer == 1:
                return answer
            else:
                continue

    def randomly_get_seat(self, lst_seats):
        seat = lst_seats.pop()
        return seat, lst_seats

    def choose_seat(self, lst_seats):
        while True:
            try:
                seat = input("Your seat is composed of an integer between 1 and 32\n"
                             "and a capital letter between A and F\n"
                             "Choose a seat in the format 1D, 13B, 32F..\n")
                # WE HAVE STOPPED HERE!!
            except ValueError:
                continue
            if seat not in lst_seats:
                print("The chosen seat is not available\n")
                continue
            else:
                lst_seats.remove(seat)
            return seat, lst_seats

    def choose_return_date(self):
        date_entry = input("Choose the date of your flight (YYYY-MM-DD)\n")
        year, month, day = map(int, date_entry.split('-'))
        date_return = datetime.date(year, month, day)
        return date_return

    def check_dates(self, date_ongoing, date_return):
        delta = date_return - date_ongoing
        if delta.days <= 0:
            print("Your return needs to be further in time")

    def prt_boarding_pass(self, fname, lname, dob, ongoing_date, ongoing_seat, coming_back_date=None, seat_comback=None):
        if coming_back_date == None:
            print("{} {} born on {} will fly on {} on seat {}".format(fname, lname, dob, ongoing_date, ongoing_seat))
        # WE NEED TO BUILD THE RETURN BOARDING PASS
        else:
            pass






