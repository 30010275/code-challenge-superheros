from flask import Flask, jsonify, request
from models import db, Hero, Power, HeroPower
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

@app.route('/')
def index():
    return {'message': 'Superheroes API'}

@app.route('/heroes')
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": h.id, "name": h.name, "super_name": h.super_name} for h in heroes])

@app.route('/heroes/<int:id>')
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify({
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": [{
                "id": hp.id,
                "hero_id": hp.hero_id,
                "power_id": hp.power_id,
                "strength": hp.strength,
                "power": {
                    "id": hp.power.id,
                    "name": hp.power.name,
                    "description": hp.power.description
                }
            } for hp in hero.hero_powers]
        })
    return jsonify({"error": "Hero not found"}), 404

@app.route('/powers')
def get_powers():
    powers = Power.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "description": p.description
    } for p in powers])

@app.route('/powers/<int:id>')
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        })
    return jsonify({"error": "Power not found"}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    try:
        power.description = data['description']
        db.session.commit()
        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        })
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        hero_power = HeroPower(
            strength=data['strength'],
            power_id=data['power_id'],
            hero_id=data['hero_id']
        )
        db.session.add(hero_power)
        db.session.commit()

        return jsonify({
            "id": hero_power.id,
            "strength": hero_power.strength,
            "power_id": hero_power.power_id,
            "hero_id": hero_power.hero_id,
            "hero": {
                "id": hero_power.hero.id,
                "name": hero_power.hero.name,
                "super_name": hero_power.hero.super_name
            },
            "power": {
                "id": hero_power.power.id,
                "name": hero_power.power.name,
                "description": hero_power.power.description
            }
        }), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
