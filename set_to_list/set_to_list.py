"""
Project:set to list converter

Author:Devam A
Date:11 july 2020

Descreption:
This program contains function that converts set into the list
Status:Tested

Bugs:
-keyword used which was eventually replaceed with another parameter in convert_set_to_list function

"""
print("\t\t\t\tset generator\n\n\n")
def generate_set():
    output_set=set()
    form_set = 1
    while(form_set != 0):
        set_elements = input("PLEASE ENTER SET ELEMENT:")
        output_set.add(set_elements)
        form_set = int(input("PLEASE ENTER 0 TO FORM SET OR ENTER ANY VALUE TO CONTINUE ADDING:"))
    print(output_set)
    return output_set

def convert_set_to_list(input_set):
    output_list = list()
    for elements in input_set:
        output_list.append(elements)
    else:
        print("set converted!")
    print(output_list)
    return output_list

my_set = {}
my_set = generate_set()
my_list = convert_set_to_list(my_set)
