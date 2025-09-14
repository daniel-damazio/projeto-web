from csv import DictWriter, DictReader

def get_all_contacts():
    contacts = []
    try:
        with open('contatos.csv','r', newline='') as file:
            reader = DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts

def save_contact(contact):
    with open('contatos.csv','a',newline='') as file:
        writer = DictWriter(file,['name','email'])

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({
         'name': contact.name,
         'email': contact.email
        })