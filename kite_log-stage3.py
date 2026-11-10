# === Stage 3: Хранилище в памяти ===
# Project: KiteLog
from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4


@dataclass
class Kite:
    name: str
    kind: str
    span: float
    wind: float
    id: str = field(default_factory=lambda: uuid4().hex)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "kind": self.kind,
            "span": self.span,
            "wind": self.wind,
        }


class KiteStore:
    def __init__(self):
        self._kites = {}

    def add(self, name, kind, span, wind):
        kite = Kite(name=name, kind=kind, span=span, wind=wind)
        self._kites[kite.id] = kite
        return kite

    def get(self, kite_id):
        return self._kites.get(kite_id)

    def list(self):
        return list(self._kites.values())
