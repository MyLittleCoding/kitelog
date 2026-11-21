# === Stage 8: Поиск по нескольким словам ===
# Project: KiteLog
from itertools import chain


def parse_query(text):
    """Разбирает строку запроса в набор обязательных и исключаемых слов.

    Обязательные слова должны встречаться в названии змея.
    Слова с префиксом «-» исключаются: их не должно быть в названии.
    """
    words = [word.strip() for word in text.split() if word.strip()]
    must = set()
    exclude = set()
    for word in words:
        if word.startswith("-"):
            exclude.add(word[1:].strip().lower())
        else:
            must.add(word.lower())
    return must, exclude


def matches(name, must, exclude):
    """Проверяет, соответствует ли название змея запросу."""
    lowered = name.lower()
    if not all(word in lowered for word in must):
        return False
    if any(word in lowered for word in exclude):
        return False
    return True


def search_kites(kites, query):
    """Ищет змеев по запросу среди их названий.

    Возвращает список объектов, чьё название удовлетворяет запросу,
    в том же порядке, что и в исходном списке.
    """
    must, exclude = parse_query(query)
    return [kite for kite in kites if matches(kite.name, must, exclude)]
