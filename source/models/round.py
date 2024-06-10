from datetime import datetime, timezone

from extensions import db


class Round(db.Model):
    __tablename__ = "round"

    id = db.Column(db.Integer, primary_key=True)
    battle_id: int = db.Column(
        db.Integer,
        db.ForeignKey("battle.id"),
        name="battle_id",
        nullable=False,
    )
    log = db.Column(db.String(100), nullable=False)

    created_at: datetime = db.Column(
        db.DateTime, default=datetime.now(timezone.utc), nullable=False
    )
