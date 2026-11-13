# === Stage 5: Связанная сущность ===
# Project: KiteLog
def new_flight(kite_id, date, wind, notes):
    return {
        "id": kite_id,
        "date": date,
        "wind": wind,
        "notes": notes,
    }


FLIGHTS = {}


def add_flight(kite_id, date, wind, notes):
    flight = new_flight(kite_id, date, wind, notes)
    FLIGHTS[flight["id"]] = flight
    return flight


def list_flights(kite_id=None):
    flights = list(FLIGHTS.values())
    if kite_id is not None:
        flights = [f for f in flights if f["id"] == kite_id]
    return sorted(flights, key=lambda f: f["date"])
