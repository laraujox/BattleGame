from marshmallow import Schema, fields


class PlayerCreationSchema(Schema):
    """Schema for Player creation request body validation"""

    name = fields.Str(required=True)
    gold = fields.Int(default=0)
    attack_value = fields.Float(required=True, validate=lambda x: x > 0)
    hit_points = fields.Float(required=True, validate=lambda x: x > 0)
    luck_value = fields.Float(required=True)


class BattleCreationSchema(Schema):
    """Schema for Battle creation request body validation"""

    attacker_name = fields.Str(required=True)
    defender_name = fields.Str(required=True)
