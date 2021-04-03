from db.run_sql import run_sql

from models.animal import Animal
from models.user import User
import repositories.user_repository as user_repository


def save(animal):
    sql = "INSERT INTO animal (animal_name, user_id, date_of_birth, animal_type, owner_contact_details, treatment_notes) VALUES (%s, %s, %s, %s %s %s) RETURNING *"
    values = [animal.animal_name, animal.date_of_birth, animal.animal_type, animal.owner_contact_details, animal.treatment_notes, animal.animal_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal


def select_all():
    animal = []

    sql = "SELECT * FROM animal"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        animal = Animal(row['animal_name'], user, row['date_of_birth'], row['animal_type'], row['owner_contact_details'], row['treatment_notes'],row['id'])
        animal.append(animal)
    return animal



def select(id):
    animal = None
    sql = "SELECT * FROM animal WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = user_repository.select(result['user_id'])
        animal = Animal(result['animal_name'], user, result['date_of_birth'], result['animal_type'], result['id'], result['owner_contact_details'], result['treatment_notes'])
    return animal


def delete_all():
    sql = "DELETE  FROM animal"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM animal WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(animal):
    sql = "UPDATE animal SET (animal_name, user_id, date_of_birth, animal_type, owner_contact_details, treatment_notes) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.animal_name, animal.user.id, animal.date_of_birth, animal.animal_type, animal.id, animal.owner_contact_details, animal.treatment_notes]
    run_sql(sql, values)
