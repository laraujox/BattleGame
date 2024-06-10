from datetime import datetime, timezone

from extensions import db


class Battle(db.Model):
    __tablename__ = "battle"

    id = db.Column(db.Integer, primary_key=True)

    player1_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    player1 = db.relationship(
        "Player", foreign_keys=[player1_id], backref="battle_player1"
    )

    player2_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    player2 = db.relationship(
        "Player", foreign_keys=[player2_id], backref="battle_player2"
    )

    winner_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=True)
    winner = db.relationship(
        "Player", foreign_keys=[winner_id], backref="battle_winner"
    )

    gold_stolen = db.Column(db.Integer, nullable=True, default=0)

    created_at = db.Column(
        db.DateTime, default=datetime.now(timezone.utc), nullable=False
    )
