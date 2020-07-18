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
from set_converter import convert_set_to_list
from set_generator import generate_set
my_set = {}
my_set = generate_set()
my_list = convert_set_to_list(my_set)
input("HURREY PROGRAM EXECUTED!!!")
