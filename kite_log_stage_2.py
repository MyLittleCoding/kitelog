# === Stage 2: Проверка полей ===
# Project: KiteLog
class KiteFieldError(Exception):
    """Базовое исключение для ошибок валидации сущности «змей»."""


def normalize_name(raw):
    """Нормализует название змея: убирает лишние пробелы и приводит к заглавной."""
    text = raw.strip()
    return text.title() if text else text


def normalize_type(raw):
    """Приводит тип к нижнему регистру и убирает лишние пробелы."""
    text = raw.strip().lower()
    return text


def normalize_span(raw):
    """Преобразует размах в число с разделителями тысяч, например '12 000' -> 12000."""
    cleaned = raw.replace(" ", "").replace(",", "").replace(".", "")
    return int(cleaned)


def normalize_wind(raw):
    """Приводит силу ветра к целому числу от 0 до 5."""
    value = int(str(raw).strip())
    if not 0 <= value <= 5:
        raise KiteFieldError("Сила ветра должна быть целым числом от 0 до 5.")
    return value


def validate_kite(raw_data):
    """Валидирует и нормализует данные сущности «змей».

    raw_data: dict с полями name, type, span, wind.
    Возвращает нормализованную запись или поднимает KiteFieldError.
    """
    data = dict(raw_data)

    name = normalize_name(data.get("name", ""))
    if not name:
        raise KiteFieldError("Название змея не может быть пустым.")

    kite_type = normalize_type(data.get("type", ""))
    if not kite_type:
        raise KiteFieldError("Тип змея не может быть пустым.")

    span = normalize_span(data.get("span", ""))
    if span <= 0:
        raise KiteFieldError("Размах змея должен быть положительным.")

    wind = normalize_wind(data.get("wind", ""))

    return {
        "name": name,
        "type": kite_type,
        "span": span,
        "wind": wind,
    }
