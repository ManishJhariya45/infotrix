contact = {}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".formet(key,contact.get(key)))
 

while True:
    Choice = int(input("1. Add the Contact \n 2. Search Contact \n 3. Display Contact \n 4. update Contact \n 5. Delete Contact 6. Exit \n Enter your Opration "))
    if Choice == 1:
        name = input ("Enter Contact Name : ")
        Phone = int(input("Enter the phone Number:  "))
        contact[name] = Phone
    elif Choice ==2:
        Search_name = input("enter the contact name: ")
        if Search_name in contact:
            print(Search_name, " contact number is ",[name])
        else:
            print(" Name is not found ")
    elif Choice == 3:
        if not contact:
            print("empty contact book")
        else: 
            display_contact()
    elif Choice == 4:
        Update_contact = input("entre the contact to be updated:  ")
        if Update_contact in contact:
            Phone = input("enter mobile number: ")
            print("contact updated")
            display_contact()
        else: 
            print("Name is not found ")
    elif Choice == 5:
        del_contact =  input("entre the contact to be deleted ")
        if del_contact in contact:
            confirm = input("Are you sure to delete this contact y/n ? ")
            if confirm == 'y' or confirm =="Y":
                contact.pop(del_contact)
            display_contact()
        else:
              print("Name is not found ")
    elif Choice == 6:
        break
    else:
        print("Phone Book is closed")