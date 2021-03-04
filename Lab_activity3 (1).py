# Marcos Tapia
#Professor Ronan Johnson
# CSS 225


#Problem 1
#   This program will ask the user if it wants to play again.
#   To play again the user will be asked to type the letter Y
#   To quit the game the user must press N
#   If the user inputs anything else it will return as invalid input.
def check_play_again():
    print("DEAD! If you would like to play again please type Y for yes and N to quit the game.")
    user_input = input("Would you like to play again?")
    if user_input == "y" or user_input == "Y":
        print("OK. Lets do it.")
    elif user_input == "n" or user_input == "N":
        print("Ok. See you later.")
    else:
        print("Invalid Input. Please try again.")
        return check_play_again()
check_play_again()

#Problem 2
#   In this program we are making a funtion that returns a boolian if we can or cant pay.
# the parameters are already set so we just need to add the response and a return statement.


def check_money(total_cost, customer_money):

    if total_cost > customer_money:
        print("False. You do not have enough.")
        return False
    elif total_cost <= customer_money:
        print("True. You have enough to pay.")
        return True

#This should print False
can_pay = check_money(107, 49)
print(can_pay)

#This should print True
can_pay = check_money(6, 88)
print(can_pay)

#Problem 3
#This program checks the reminder of n

def ZipZap(n):

    if n%5 == 0 and n%7 == 0:
        print("ZipZap")
    elif n%5 == 0:
        print("Zip")
    elif n%7 == 0:
        print("Zap")
    else:
        print(n)
ZipZap(35)
