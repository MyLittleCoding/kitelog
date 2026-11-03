# === Stage 1: Каркас модуля ===
# Project: KiteLog
from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Kite:
    name: str
    kind: str
    span: float
    wind: int


def sample_kites() -> List[Kite]:
    return [
        Kite("Молния", "алмазный", 1.8, 3),
        Kite("Полуночник", "бридж", 2.4, 4),
        Kite("Хвостик", "хвостовой", 1.2, 2),
    ]


def main() -> None:
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"KiteLog — журнал воздушных змеев и ветра")
    print(f"Дата: {today}")
    print()
    print("Демо-модели:")
    for kite in sample_kites():
        print(f"  [{kite.kind}] {kite.name} — размах {kite.span} м, ветер {kite.wind} м/с")
