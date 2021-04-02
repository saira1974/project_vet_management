DROP TABLE IF EXISTS animal;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id SERIAL FOREIGN KEY,
  vet_name VARCHAR(255),
);

CREATE TABLE animal (
  id SERIAL PRIMARY KEY,
  animal_name VARCHAR(255),
  date_of_birth VARCHAR(255),
  owner_contact_details TEXT,
  treatment_notes TEXT,
  animal_id INT REFERENCES users(id)
);