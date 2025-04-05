from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():
    db.drop_all()
    db.create_all()

    h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    h2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    h3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    
    p1 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
    p2 = Power(name="super strength", description="gives the wielder incredible strength")
    p3 = Power(name="wall crawling", description="gives the wielder the ability to stick to and climb walls")

    db.session.add_all([h1, h2, h3, p1, p2, p3])
    db.session.commit()

    hp1 = HeroPower(hero_id=h1.id, power_id=p1.id, strength="Strong")
    hp2 = HeroPower(hero_id=h2.id, power_id=p2.id, strength="Average")
    hp3 = HeroPower(hero_id=h3.id, power_id=p3.id, strength="Weak")

    db.session.add_all([hp1, hp2, hp3])
    db.session.commit()
