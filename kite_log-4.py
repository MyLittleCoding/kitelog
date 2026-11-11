# === Stage 4: Редактирование записей ===
# Project: KiteLog
def update_kite(kite_id, changes):
    """Редактирует змей по id, применяя только допустимые поля.

    Возвращает кортеж (успех, сообщение, объект_змей). При неудаче
    объект_змей не возвращается.
    """
    ALLOWED_FIELDS = {
        "name": str,
        "type": str,
        "span": (int, float),
        "wind": (int, float),
    }

    if "id" in changes:
        return False, "Поле id нельзя изменять", None

    if not isinstance(changes, dict):
        return False, "Изменения должны быть словарём", None

    if len(changes) != 1:
        return False, "Можно изменить только одно поле за раз", None

    field, value = next(iter(changes.items()))

    if field not in ALLOWED_FIELDS:
        return False, f"Поле '{field}' не существует для змея", None

    if not isinstance(value, ALLOWED_FIELDS[field]):
        return False, f"Значение для '{field}' имеет неподдерживаемый тип", None

    kites = _load_kites()

    target = _find_by_id(kites, kite_id)
    if target is None:
        return False, f"Змей с id {kite_id} не найден", None

    target[field] = value

    _save_kites(kites)

    return True, "Змей обновлён", target


def _find_by_id(kites, kite_id):
    for kite in kites:
        if kite.get("id") == kite_id:
            return kite
    return None


def _load_kites():
    try:
        with open("kites.json", "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _save_kites(kites):
    with open("kites.json", "w", encoding="utf-8") as handle:
        json.dump(kites, handle, ensure_ascii=False, indent=2)
