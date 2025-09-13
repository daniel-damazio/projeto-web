from flask import Flask, request, render_template
from classes import UserContact
from functions import save_contact

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["user_name"]
        useremail = request.form["user_email"]
        contact = UserContact(username,useremail)
        save_contact(contact)
        return f"Usuário {username} e {useremail} registrado com sucesso!"
    return render_template("index.html")


if __name__ == "__main__":
    app.run()