import unittest
from models.animal import Animal

class TestAnimal(unittest.TestCase):


    def setUp(self):
        self.animal = Animal("olly", "15 April 2010", "bengal", "07311811098", "rat bite")
    
    def test_animal_name(self):
        self.assertEqual("olly", self.animal.animal_name)
    
    def test_date_of_birth(self):
        self.assertEqual("15 April 2010", self.animal.date_of_birth) 
    
    def test_animal_type(self):
        self.assertEqual("bengal", self.animal.animal_type)

    def test_owner_contact_details(self):
        self.assertEqual("07311811098", self.animal.owner_contact_details)
    
    def test_treatment_notes(self):
        self.assertEqual("rat bite", self.animal.treatment_notes)

   
    
    