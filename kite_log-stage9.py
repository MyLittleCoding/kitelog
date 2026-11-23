# === Stage 9: Теги ===
# Project: KiteLog
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class KiteTag:
    name: str
    color: str = "#888888"


@dataclass
class Kite:
    name: str
    type: str
    span: float
    wind: str
    tags: List[KiteTag] = field(default_factory=list)

    def add_tag(self, name: str, color: Optional[str] = None) -> KiteTag:
        if not name:
            raise ValueError("Тег не может быть пустым")
        for tag in self.tags:
            if tag.name.lower() == name.lower():
                if color is not None:
                    tag.color = color
                return tag
        tag = KiteTag(name=name, color=color or "#888888")
        self.tags.append(tag)
        return tag

    def remove_tag(self, name: str) -> bool:
        before = len(self.tags)
        self.tags = [t for t in self.tags if t.name.lower() != name.lower()]
        return len(self.tags) != before

    def find_tag(self, name: str) -> Optional[KiteTag]:
        for tag in self.tags:
            if tag.name.lower() == name.lower():
                return tag
        return None


class KiteTagStore:
    def __init__(self):
        self._kites: Dict[str, Kite] = {}

    def add_kite(self, kite: Kite) -> None:
        self._kites[kite.name] = kite

    def get_kite(self, name: str) -> Optional[Kite]:
        return self._kites.get(name)

    def add_tag(self, kite_name: str, name: str, color: Optional[str] = None) -> Optional[KiteTag]:
        kite = self.get_kite(kite_name)
        if not kite:
            return None
        return kite.add_tag(name, color)

    def remove_tag(self, kite_name: str, name: str) -> bool:
        kite = self.get_kite(kite_name)
        if not kite:
            return False
        return kite.remove_tag(name)

    def find_by_tag(self, name: str) -> List[Kite]:
        result = []
        for kite in self._kites.values():
            if kite.find_tag(name):
                result.append(kite)
        return result

    def list_tags(self) -> List[KiteTag]:
        seen: Dict[str, KiteTag] = {}
        for kite in self._kites.values():
            for tag in kite.tags:
                if tag.name.lower() not in seen:
                    seen[tag.name.lower()] = tag
        return list(seen.values())
