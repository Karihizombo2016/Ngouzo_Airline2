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
                       "or q to quit.\n")

    while user_input != 'q':
        plane = Plane()
        print(plane)
        if user_input == 'a':
            first_name = input("Enter your first name\n")
            last_name = input("Enter your last name\n")
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
