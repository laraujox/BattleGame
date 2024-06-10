from extensions import db


class Player(db.Model):
    __tablename__ = "player"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    gold = db.Column(db.Integer, nullable=False, default=0)
    attack_value = db.Column(db.Integer, nullable=False)
    hit_points = db.Column(db.Integer, nullable=False)
    luck_value = db.Column(db.Integer, nullable=False)
