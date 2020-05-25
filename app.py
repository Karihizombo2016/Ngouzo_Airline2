from plane import Plane
from customer import Customer




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
    print()
    while user_input != 'q':
        plane = Plane()
        print(plane)
        if user_input == 'a':
            first_name = input("Enter your first name\n").strip()
            last_name = input("Enter your last name\n").strip()
            customer = Customer(first_name, last_name)
            print(customer)
            # Get DOB
            dob = customer.get_convert_date("DOB")
            print("DOB: {}".format(dob))
            age = int(customer.check_age(dob))
            if age < 18:
                import sys
                sys.exit("You are only {} years old.\n"
                         "You cannot book a flight ticket without your parents!\n"
                         "Bye.".format(age))
            else:
                print("You are {} years old. You can carry on!".format(age))
                # Decide whether one way or return
                num_flight = customer.choose_one_way_or_return()
                # Make seats
                lst_seats = plane.make_seats()
                # One way flight
                if num_flight == 1:
                    ongoing_date = customer.choose_ongoing_date()
                    # Choose your ongoing seat
                    ongoing_seat, lst_seats = customer.choose_random_manual_seat(lst_seats)
                    # Print boarding pass
                    customer.prt_boarding_pass(first_name, last_name, dob, ongoing_date, ongoing_seat)

                # Return ticket
                # WE HAVE STOPPED HERE
                elif num_flight == 2:
                    ongoing_date = customer.choose_ongoing_date()
                    comeback_date = customer.choose_comeback_date(ongoing_date)
                    ongoing_seat, lst_seats = customer.choose_random_manual_seat(lst_seats, "ongoing seat")
                    print("Your ongoing seat is {}".format(ongoing_seat))
                    comeback_seat, lst_seats = customer.choose_random_manual_seat(lst_seats, "comeback seat")
                    customer.prt_boarding_pass(first_name, last_name, dob, ongoing_date, ongoing_seat,
                                               comeback_date, comeback_seat)
            # The list of seats is not updated from one round to another!!
            # Check if the ongoing_seat is different from comeback_seat!





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
