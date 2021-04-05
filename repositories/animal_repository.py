from db.run_sql import run_sql

from models.animal import Animal
from models.user import User
import repositories.user_repository as user_repository


def save(animal):
    sql = "INSERT INTO animals (animal_name, user_id, date_of_birth, animal_type, owner_contact_details, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [animal.animal_name, animal.user.id, animal.date_of_birth, animal.animal_type, animal.owner_contact_details, animal.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal


def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        animal = Animal(row['animal_name'],user, row['date_of_birth'], row['animal_type'], row['owner_contact_details'], row['treatment_notes'],row['id'])
        animals.append(animal)
    return animals



def select(id):
    animals = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        users = users_repository.select(result['user_id'])
        animals = Animals(result['animal_name'], user, result['date_of_birth'], result['animal_type'], result['id'], result['owner_contact_details'], result['treatment_notes'])
    return animals


def delete_all():
    sql = "DELETE  FROM animals"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(animals):
    sql = "UPDATE animals SET (animal_name, user_id, date_of_birth, animal_type, owner_contact_details, treatment_notes) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animals.animal_name, animals.user.id, animals.date_of_birth, animals.animal_type, animals.id, animals.owner_contact_details, animals.treatment_notes]
    run_sql(sql, values)
