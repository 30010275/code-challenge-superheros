#  Superheroes API
 simple flask app  **Superheroes**, and their **Powers**, and the relationship between them.
 
 Setup Instructions

### 1. Clone the repository

### 2. Set up virtual environment
pipenv install
pipenv shell
```

### 3. Run the app
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py
flask run
```

##  Testing with Postman

1. Open Postman
2. Run all the routes to confirm functionality

##API Endpoints

### Heroes
- `GET /heroes`  
  Returns a list of all heroes.
- `GET /heroes/<id>`  
  Returns a single hero and their powers.  
  If not found: `{ "error": "Hero not found" }`

### Powers
- `GET /powers`  
  Returns a list of all powers.

- `GET /powers/<id>`  
  Returns a single power.  
  If not found: `{ "error": "Power not found" }`

- `PATCH /powers/<id>`  
  Update a power's description.  
  Validates that the description is at least 20 characters.  
  Errors:  
  - Not found: `{ "error": "Power not found" }`  
  - Validation fail: `{ "errors": ["validation errors"] }`

### Hero Powers
- `POST /hero_powers`  
  Creates a new hero-power relationship.  
  Request body:
  ```json
    
