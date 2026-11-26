# === Stage 10: Группировка ===
# Project: KiteLog
def group_by_type(kites):
    groups = {}
    for kite in kites:
        groups.setdefault(kite['type'], []).append(kite)
    return groups


def count_by_type(kites):
    counts = {}
    for kite in kites:
        counts[kite['type']] = counts.get(kite['type'], 0) + 1
    return counts


def summarize(kites):
    counts = count_by_type(kites)
    total = len(kites)
    for kite_type in sorted(counts):
        print(f"{kite_type}: {counts[kite_type]}")
    print(f"Всего: {total}")


if __name__ == "__main__":
    sample_kites = [
        {'name': 'Орёл', 'type': 'Парапет', 'span': 2.0, 'wind': 5},
        {'name': 'Лебедь', 'type': 'Парапет', 'span': 2.5, 'wind': 6},
        {'name': 'Змийка', 'type': 'Лента', 'span': 1.0, 'wind': 3},
        {'name': 'Буревестник', 'type': 'Парапет', 'span': 3.0, 'wind': 7},
    ]
    summarize(sample_kites)
