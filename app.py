from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)



@app.route("/")
def homepage():
    """Show homepage listing pets."""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)



@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Shows form to add new pet; submits new pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        
        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    else:
        # reloads the form showing the previous data and error messages
        return render_template("new.html", form=form)
    

    
@app.route("/<int:id>", methods=["GET", "POST"])
def view_edit_pet(id):
    """Shows pet details and allows editing of them"""

    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("view_edit.html", form=form, pet=pet)
