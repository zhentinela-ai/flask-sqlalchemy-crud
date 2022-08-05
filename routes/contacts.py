from flask import Blueprint

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    return "contacts list"


@contacts.route("/new")
def add_contacr():
    return "saving a contact"
