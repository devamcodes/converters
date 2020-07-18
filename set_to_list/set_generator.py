
def generate_set():
    print("\t\t\t\tset generator\n\n\n")
    output_set=set()
    form_set = 1
    while(form_set != 0):
        set_elements = input("PLEASE ENTER SET ELEMENT:")
        output_set.add(set_elements)
        form_set = int(input("PLEASE ENTER 0 TO FORM SET OR ENTER ANY VALUE TO CONTINUE ADDING:"))
    print(output_set)
    return output_set
