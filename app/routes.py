from flask import Blueprint, jsonify, request
from .models import db, Hero, Power, HeroPower

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Superheroes API!"})

@api.route('/heroes', methods=['GET'])
def get_heroes():
    return jsonify([hero.to_dict() for hero in Hero.query.all()])

@api.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict())

@api.route('/powers', methods=['GET'])
def get_powers():
    return jsonify([p.to_dict() for p in Power.query.all()])

@api.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

@api.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    try:
        power.description = data.get("description", power.description)
        db.session.commit()
        return jsonify(power.to_dict())
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()

        hero = Hero.query.get(hero_power.hero_id)
        return jsonify(hero.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
