people = {
    "Brian": "+1-322-564-1001",
    "Miles": "+1-322-564-1293",
    "Ron": "+1-322-564-1099",
}
if "__name__" == "__main__":
    name = input("Name: ")
    if name.capitalize() in people:
        print(f"Number: {people[name.capitalize()]}")
    else:
        print("Contact not found".upper())
        ask = input("Do you want to add Number to phonebook?: ")
        if ask.lower() in ["yes", "y"]:
            new_name = input("Name: ")
            new_num = input("Number: ")
            new_contact = {new_name: new_num}
            people.update(new_contact)
        elif ask.lower() in ["no", "n"]:
            view_pbook = input("Do you want to view contacts?: ")
            if view_pbook.lower() in ["yes", "y"]:
                for person in people:
                    print(f"{person}: {people[person]}")
            elif view_pbook.lower() in ["no", "n"]:
                print("Alright, Have a Nice Day")
