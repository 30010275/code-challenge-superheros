 simple Flask API to manage superheroes and their powers.

Features
View all heroes and powers
Get hero details with powers
Update power descriptions
Assign powers to heroes

Installation 
Clone the repository:
Create and activate virtual environment:
python3 -m venv env
source env/bin/activate

Install dependencies:
pip install -r requirements.txt
Set up and seed the database:
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
python seed.py

Run the server:

flask run

Usage

Use Postman to test the following endpoints:
GET /heroes – list all heroes
GET /heroes/<id> – view a hero with their powers
GET /powers – list all powers
GET /powers/<id> – view a specific power
PATCH /powers/<id> – update a power's description
POST /hero_powers – assign a power to a hero

