from bot_classes import AddressBook, Record


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format for add. Please use: add [name] [phone]"
    name, phone = args
    contacts.add_record(Record(name=name,))
    contacts[name].add_phone(phone)
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format for change. Please use: change [name] [new phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command format for phone. Please use: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def add_birthday(args, contacts):
    if len(args) != 2:
        return "Invalid command format for add-birthday. Please use: add-birthday [name] [DD.MM.YYYY]"
    name, birth_date = args
    try:
        contacts.add_birthday(name, birth_date)
        return "Birthday added."
    except ValueError as e:
        return str(e)


def show_birthday(args, contacts):
    if len(args) != 1:
        return "Invalid command format for show-birthday. Please use: show-birthday [name]"
    name = args[0]
    contact = contacts.find(name)
    if contact:
        if contact.birthday:
            return contact.get_birthday()
        else:
            return "Birthday not set for this contact."
    else:
        return "Contact not found."


def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit",]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            birthdays = contacts.get_birthdays_per_week()
            if birthdays:
                for day, names in birthdays.items():
                    print(f"{day}: {', '.join(n.value for n in names)}")
            else:
                print("No upcoming birthdays in the next week.")
        else:
                print("Invalid command.")


if __name__ == "__main__":
    main()
