import pdb
from models.animal import Animal
from models.user import User

import repositories.animal_repository as animal_repository
import repositories.user_repository as user_repository

animal_repository.delete_all()
user_repository.delete_all()

user1 = User("Saira", "Richardson")
user_repository.save(user1)
user2 = User("Danny", "Richardson")
user_repository.save(user2)

user_repository.select_all()

animal_1 = Animal("Olly", user1, "date of birth","cat", "07311811098", "rat bite")
animal_repository.save(animal_1)

animal_2 = Animal("Ellie", user2, "19-09-19", "dog", "07311811098", "sore paw")
animal_repository.save(animal_2)
all_users = user_repository.select_all()
all_animals = animal_repository.select_all()

pdb.set_trace()
