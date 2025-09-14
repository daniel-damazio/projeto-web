from flask import Flask, request, render_template, redirect
from classes import UserContact
from functions import save_contact, get_all_contacts

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["user_name"]
        useremail = request.form["user_email"]
        contact = UserContact(username,useremail)
        save_contact(contact)
        return redirect('/')
    return render_template("index.html")

@app.route('/contatos', methods=["GET"])
def contacts():
    all_contacts = get_all_contacts()
    return render_template("contacts.html", contacts=all_contacts)

if __name__ == "__main__":
    app.run()