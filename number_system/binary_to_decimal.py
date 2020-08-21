"""
Project:Binary to Decimal
Author:Devam A

Description:converts Binary numbers to Decimal numbers
Steps:
1. take input of binary numbers
2.

"""
"for egd -techmax"
"for maths tatmegrog"
"refrence darshan institute"
# TODO:take user input in different bits so you can work on single bit at a time(use while loop in input).
# TODO:use list to save the input and use list splitting to remove comas in showing the input binary number to user.
# TODO:convert each bit to decimal by multiplyinng it with 2 power n and print it out.
def decimal_converter():
    # TODO:this user_input is integer but this function needs string.
    for numbers in user_input_list:
        print(numbers * 2^n)
print("\t\t\t\t\tTHIS CONVERTS BINARY INTO DECIMAL\n")
user_choice = 1
while user_choice == 1:
    user_input = bin(int(input("enter the bit:")))
    user_input_list = []
    user_input_list.append(user_input)
    print(f"this is your binary number {user_input_list}.replace(',')")
#TODO:PLACE THE REPLACE STATEMENT AT THE RIGTH PLACE TO REMOVE THE COMMAS IN PRINT COMMAND TO SHOW THE USER FULL NUMBER HE/SHE WANTED TO ENTER.
    n = range(len(user_input_list))
    decimal_converter()
    user_choice = input("enter 1 to continue or 0 to end")
else:
    print("end!!!")