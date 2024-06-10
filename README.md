### BattleGame API

Welcome to the BattleGame API documentation. This API allows you to create battles between players and register new players. Below are the available endpoints along with their request and response formats.

### Folder Structure

- **error_handling**: Contains exceptions and request schema validations.
- **models**: Contains SQLAlchemy ORM models for each entity.
- **repositories**: Handles database changes (add, get, list) for each model.
- **services**: Contains all application business rules.
- **views**: Contains the client layer, where all endpoints are defined.

---

## Installation

### Step-by-Step Installation Guide

1. **Create Virtual Environment**  
   ```sh
   make create_venv
   ```

2. **Activate Virtual Environment**  
   ```sh
   . venv/bin/activate
   ```  

3. **Install Dependencies**  
   ```sh
   make install
   ```  

4. **Start the Flask application and the local database.**  
   ```sh
   make run
   ```

5. **Execute any pending database migrations.**  
   ```sh
   make db-upgrade
   ```

---
### Create Battle

Creates a new battle between two players.

- **URL**: `/battle`
- **Method**: `POST`

#### Request Body

```json
{
    "attacker_name": "HotBarbecu3",
    "defender_name": "Vegan2"
}
```

#### Response Body

```json
{
    "winner": "HotBarbecu3",
    "gold_stolen": 50,
    "round_log": [
        "HotBarbecu3 attacked Vegan2 for 100.0 damage",
        "Vegan2 attacked HotBarbecu3 for 50.0 damage",
        "HotBarbecu3 attacked Vegan2 for 75.0 damage",
        "Vegan2 attacked HotBarbecu3 for 25.0 damage",
        "HotBarbecu3 attacked Vegan2 for 62.5 damage",
        "HotBarbecu3 won the battle and stole 149 gold from Vegan2"
    ]
}
```

#### Status Codes

- `200 OK`: Successful battle creation.
- `400 Bad Request`: Invalid request body format.

---

### Create Player

Registers a new player with the specified attributes.

- **URL**: `/player`
- **Method**: `POST`

#### Request Body

```json
{
    "name": "HotBarbecu3",
    "gold": 100,
    "attack_value": 50,
    "hit_points": 200,
    "luck_value": 7
}
```

#### Response Body

```json
{
    "message": "Player created successfully!"
}
```

#### Status Codes

- `200 OK`: Successful player registration.
- `400 Bad Request`: Invalid request body format or player data.

---

#### Notes

- Errors related to player validation or custom exceptions are returned with appropriate status codes and error messages.
- For any questions or issues, please contact the API developers.

---

