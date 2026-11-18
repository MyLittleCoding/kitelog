# === Stage 7: Сортировка записей ===
# Project: KiteLog
from datetime import datetime


def sort_by_name(kites, reverse=False):
    return sorted(kites, key=lambda kite: kite["name"], reverse=reverse)


def sort_by_created(kites, reverse=False):
    return sorted(
        kites,
        key=lambda kite: kite["created_at"] or datetime.min,
        reverse=reverse,
    )


def sort_by_created_then_name(kites, reverse=False):
    return sorted(
        kites,
        key=lambda kite: (
            kite["created_at"] or datetime.min,
            kite["name"],
        ),
        reverse=reverse,
    )
