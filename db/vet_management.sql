DROP TABLE animals;
DROP TABLE users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  vet_name VARCHAR(255)
);

CREATE TABLE animals (
  id SERIAL PRIMARY KEY,
  animal_name VARCHAR(255),
  date_of_birth VARCHAR(255),
  animal_type VARCHAR(255),
  owner_contact_details TEXT,
  treatment_notes TEXT,
  user_id INTEGER REFERENCES users(id)
);