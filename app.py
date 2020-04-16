from plane import Plane
from customer import Customer


# miki = Customer(first_name="Miki", last_name="Madi", dob="1980-04-17")
#
# print(miki)
#
# dt_flight = miki.choose_date()
# print(dt_flight)

def menu():
    '''
    We need to modify the script so that once we have chosen a date it is automatically convert into the right format.
    Ask the customer her first_name, last_name, dob.
    Check if the customer does not exit in the dictionary of customers.
    If not, create a new entry in the dictionary.

    Ask which action the client want to do:
     - q: quit
     - d: choose date of flight (ongoing and return). The system will check the dates.
     - s: choose a seat in the plane (ongoing and return). The system will check whether seats are available.
     '''

    user_input = input("Enter a to add new passenger,\n"
                       "d to delete a passenger,\n"
                       "l to see the list of passenger,\n"
                       "s to see the list of available seats,\n"
                       "save to save\n"
                       "or q to quit.\n").strip()

    while user_input != 'q':
        plane = Plane()
        print(plane)
        if user_input == 'a':
            first_name = input("Enter your first name\n").strip()
            last_name = input("Enter your last name\n").strip()
            customer = Customer(first_name, last_name)
            print(customer)
            dob = customer.get_dob()

            # dob = customer.convert_str_date(dob)
            # first_name = plane.get_first_name()
            # last_name = plane.get_last_name()
            # dob = plane.get_dob()

            dob = customer.convert_into_date(dob)
            while dob == 0:
                print("Your DOB is wrong!")
                dob = customer.get_dob()
                dob = customer.convert_into_date(dob)

                # dob = customer.convert_into_date(dob)
                # print("Your DOB is wrong!: {}".format(dob))

            else:
                print("DOB: {}".format(dob))
                age = int(customer.check_dob(dob))
                if age < 18:
                    import sys
                    sys.exit("You are only {} years old.\n"
                             "You cannot book a flight ticket without your parents!\n"
                             "Bye.".format(age))
                else:
                    print("You are {} years old. You can carry on.".format(age))
                    # Decide whether one way or return
                    num_flight = customer.choose_one_way_or_return()
                    # WE HAVE STOPPED HERE. WE NEED TO MODIFY THE CODE TO ONLY ACCEPT 1 OR 2
                    # One way ticket
                    if num_flight == 1:
                        ongoing_date = customer.choose_ongoing_date()
                        ongoing_date = customer.convert_into_date(ongoing_date)
                        while ongoing_date == 0:
                            print("Your ongoing date is wrong!")
                            ongoing_date = customer.choose_ongoing_date()
                            ongoing_date = customer.convert_into_date(ongoing_date)
                        else:
                            # Get a list of seats
                            lst_seats = plane.make_seats()
                            # Pick a seat randomly
                            seat_customer = customer.pick_seat(lst_seats)
                            print("Customer {} {}, {} years old will fly on {} on seat {}"
                                  .format(first_name, last_name, age, ongoing_date, seat_customer))



                    # lst_seats = plane.make_seats()
                    # print("Here is the list of available seats: {}".format(lst_seats))
                # WE HAVE STOPPED HERE. WHAT DO WE DO AFTER WHEN THE PASSENGER IS > 18?


                # print("You are {} years old".format(age))



# HOW ARE WE SAVING THE DATA? JSON, LIST?

        elif user_input == 'd':
            pass
        elif user_input == 'l':
            pass
        elif user_input == 's':
            pass

        user_input = input("Enter a to add new passenger,\n"
                           "d to delete a passenger,\n"
                           "l to see the list of passenger,\n"
                           "s to see the list of available seats,\n"
                           "save to save\n"
                           "or q to quit.\n")


menu()
