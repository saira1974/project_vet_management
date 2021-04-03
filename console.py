import pdb
from models.animals import Animals
from models.users import Users

import repositories.animals_repository as animals_repository
import repositories.users_repository as users_repository

animals_repository.delete_all()
users_repository.delete_all()

user1 = User("Saira", "Richardson")
users_repository.save(user1)
user2 = User("Danny", "Richardson")
users_repository.save(user2)

users_repository.select_all()

animal_1 = Animal("Olly", user1)
animals_repository.save(animal_1)

animal_2 = Animal("Ellie", user2)
animals_repository.save(animal_2)


pdb.set_trace()
