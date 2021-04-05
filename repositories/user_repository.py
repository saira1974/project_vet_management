from db.run_sql import run_sql

from models.user import User
from models.animal import Animal

def save(users):
    sql = "INSERT INTO users (vet_name) VALUES (%s) RETURNING *"
    values = [users.vet_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return users

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        users = User(row['vet_name'], row['id'] )
        users.append(users)
    return users

def select(id):
    users = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        users = Users(result['vet_name'], result['id'] )
    return users

def delete_all():
    sql = "DELETE  FROM users"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(users):
    sql = "UPDATE users SET (vet_name) = (%s) WHERE id = %s"
    values = [users.vet_name, user.id]
    run_sql(sql, values)

def animals(users):
    animals = []

    sql = "SELECT * FROM animals WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        animals = Animals(row['animal_name'], row['user_id'], row['date_of_birth'], row['animal_type'], row['id'], [owner_contact_details], [treatment_notes] )
        animals.append(animals)
    return animals
