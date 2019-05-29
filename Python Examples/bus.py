# this is the bus project. It's a bitch..

def show_menu():
    #print welcome and show menu of options
    print("Welcome!")
    print("To Book, enter '1'")
    print("To Pay, enter '2'")
    print("To View info, enter '3'")
    # Ask for input & remember choiceself.
    choice = input("Please enter: ")
    if choice == "1":
        print("Booking! Please wait.. ")
        book()
    elif choice == "2":
        print("Payment! Please wait.. ")
        # pay()
    elif choice == "3":
        print("Info! Please wait.. ")
        # info()
    elif choice != "1" "2" "3" :
        print("Not a choice, fuckwad! Try again!")
        show_menu()
        #probably a counter!


def book():
    bus = ['','','','','','','','','','']
    print(bus)
    #('', = empty | 'x', = taken seat)
    # check for empty seats
    i=0
    for seat in bus:
        if seat == '':
            bus[i] = 'x'
        i=+1
    print(bus)

        #Retrieve the index
        # print("No seats. You're fucked. Go away. ")

        # print("Yes, a seat is open! ")
        # print("Would you like to book a seat? ")
        # print("To book, enter '1'")
        # print("to fuck off, enter '2'")
        # choice = input("Please enter: ")
        # if choice == "1":
        #     print("whoo!")
        #     print(bus[0])
        #     bus[0] == "x"
        #     print(bus[0])
        #     # elif bus[1] == '':
        #     #     bus[1] ==
        # elif choice == "2":
        #     print("nooo!")

    # else:

    # ask if they'd like to book a seat
    # change empty seat to taken seats
    # offer option to cancel, and not change seats

# def pay():
    # no connection , honor system with book() function
    # print a message with he price of a ticket $10
    # ask how many seats have been booked.
    # ask for payment in numbers devisible by 5, 10, 20, 50, 100
    # check for payment acceptablility, two fives, one ten, twenty fifty etc
    # if not, print error messageself.
    # calcuate and issue change
    # thank you message
    # exit

# def info():
    # show info about the bus
    # display how many seats are availible
    #

def main():
    show_menu()
    #show the menu (see show menu)
    #parting message

main()
