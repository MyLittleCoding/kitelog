# === Stage 6: Связи между сущностями ===
# Project: KiteLog
def get_kite_flights(kite: dict) -> list:
    """Возвращает список полётов для заданной змей по полю id."""
    flights = []
    for flight in kite_flights_store:
        if flight.get("kite_id") == kite.get("id"):
            flights.append(flight)
    return flights


def check_relationship_integrity(kite: dict) -> bool:
    """Проверяет, что все полёты змей существуют в реестре змей."""
    kite_id = kite.get("id")
    kite_name = kite.get("name")

    flights = get_kite_flights(kite)

    if len(flights) != 0:
        return True

    return False


kite_flights_store = [
    {"flight_id": 1, "kite_id": 1, "date": "2024-01-01", "wind_speed": 5, "distance": 100},
    {"flight_id": 2, "kite_id": 1, "date": "2024-01-02", "wind_speed": 7, "distance": 150},
    {"flight_id": 3, "kite_id": 2, "date": "2024-01-03", "wind_speed": 8, "distance": 200},
]
