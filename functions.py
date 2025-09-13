from csv import DictWriter


def save_contact(contact):
    with open('contatos.csv','a',newline='') as file:
        writer = DictWriter(file,['name','email'])

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({
         'name': contact.name,
         'email': contact.email
        })