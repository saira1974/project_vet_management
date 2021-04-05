from flask import Flask, render_template, request, redirect
import repositories.animal_repository as animal_repository
import repositories.user_repository as user_repository
from models.animal import Animal

from flask import Blueprint

animals_blueprint = Blueprint("animals", __name__)
# RESTful CRUD Routes

# INDEX
# GET '/animal'
@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all() # NEW
    return render_template("animals/index.html", all_animals = animals)


# NEW
# GET '/animals/new'
@animals_blueprint.route('/animals/new')
def new():
    users = user_repository.select_all() 
    return render_template("animals/new.html", users = users)


# CREATE
# POST '/animals'
@animals_blueprint.route("/animals", methods=["POST"])
def create():
    animal_name = request.form["animal_name"]
    user_id = request.form["user_id"]
    date_of_birth = request.form["date_of_birth"]
    animal_type = request.form["animal_type"]
    owner_contact_details = request.form["owner_contact_details"]
    treatment_notes = request.form["treatment_notes"]
    user = user_repository.select(user_id)
    animal = Animal(animal_name, user, date_of_birth, animal_type, owner_contact_details, treatment_notes)
    animal_repository.save(animal)
    return redirect("/animals")


# SHOW
# GET '/animal/<id>'
@animals_blueprint.route("/animals/<id>")
def show(id):
    animals = animals_repository.select(id)
    return render_template("animals/show.html", animals=animals)


# EDIT
# GET '/animals/<id>/edit'
@animals_blueprint.route("/animals/<id>/edit")
def edit(id):
    animals = animals_repository.select(id)
    users = users_repository.select_all()
    return render_template("animals/edit.html", animals = animals, users=users) 


# UPDATE
# PUT '/animals/<id>'
@animals_blueprint.route("/animals/<id>", methods=["POST"])
def update(id):
    animal_name = request.form["animal name"]
    user_id = request.form["user_id"]
    date_of_birth = request.form["date_of_birth"]
    animal_type = request.form["animal type"]
    owner_contact_details = request.form["owner_contact_details"]
    treatment_notes = request.form["treatment_notes"]
    users = users_repository.select(user_id)
    animals = Animals(animal_name, users, date_of_birth, animal_type, owner_contact_details, treatment_notes, id)
    animals_repository.update(animals)
    return redirect(f"/animals/{id}")

# DELETE
# DELETE '/animals/<id>'

@animals_blueprint.route("/animals/<id>/delete", methods=["POST"])
def delete(id):
    animals_repository.delete(id)
    return redirect("/animals")