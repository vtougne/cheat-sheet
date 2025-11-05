#!/usr/bin/env python3
import json
import re
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

# Fuseau horaire France
TZ_PARIS = ZoneInfo("Europe/Paris")

# Entrée : règles anglaises avec heure et cycle
planning_rules = {
    "patch_app1": {"rule": "3rd Tuesday March 2025", "hour": "02:00", "cycle": "3 months"},
    "patch_app2": {"rule": "2nd Thursday June 2025", "hour": "04:30", "cycle": "6 months"},
    "patch_app3": {"rule": "1st Monday September 2025", "hour": "01:15", "cycle": "12 months"}
}

# Durée de génération
YEARS_TO_GENERATE = 2

# Tables de correspondance
WEEKDAY_TO_INDEX = {
    "monday": 0, "tuesday": 1, "wednesday": 2,
    "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6
}

MONTH_TO_INDEX = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12
}


def parse_rule(rule_str):
    """Extrait nᵉ jour, jour de semaine, mois et année depuis la règle."""
    match = re.match(r"(\d+)(st|nd|rd|th)\s+(\w+)\s+(\w+)\s+(\d{4})", rule_str.strip(), re.IGNORECASE)
    if not match:
        raise ValueError(f"Invalid rule format: {rule_str}")
    week_num = int(match.group(1))
    weekday = WEEKDAY_TO_INDEX[match.group(3).lower()]
    month = MONTH_TO_INDEX[match.group(4).lower()]
    year = int(match.group(5))
    return week_num, weekday, month, year


def nth_weekday(year, month, weekday, n):
    """Renvoie la date du n-ième `weekday` dans un mois donné."""
    count = 0
    for day in range(1, 32):
        try:
            date = datetime(year, month, day)
        except ValueError:
            break
        if date.weekday() == weekday:
            count += 1
            if count == n:
                return date.date()
    return None


def add_months(orig_date, months):
    """Ajoute des mois à une date."""
    year = orig_date.year + (orig_date.month + months - 1) // 12
    month = (orig_date.month + months - 1) % 12 + 1
    day = min(orig_date.day, 28)  # évite problèmes de fin de mois
    return orig_date.replace(year=year, month=month, day=day)


def generate_planning(rules, years=2):
    """Génère le planning pour les règles fournies."""
    planning = []
    now = datetime.now()
    max_date = now.astimezone(TZ_PARIS).replace(year=now.year + years)

    for app, data in rules.items():
        rule = data["rule"]
        hour_str = data.get("hour", "00:00")
        cycle_str = data.get("cycle", "3 months")

        n, weekday, month, year = parse_rule(rule)
        hour, minute = map(int, hour_str.split(":"))

        # Date de départ du cycle
        start_date = nth_weekday(year, month, weekday, n)
        if not start_date:
            continue

        start_dt = datetime.combine(start_date, time(hour, minute)).replace(tzinfo=TZ_PARIS)

        # Extraction du nombre de mois du cycle
        match = re.match(r"(\d+)\s+months", cycle_str.strip(), re.IGNORECASE)
        cycle_months = int(match.group(1)) if match else 3

        # Génération
        dt = start_dt
        while dt <= max_date:
            planning.append({
                "app": app,
                # "datetime": dt.isoformat()
                "datetime": dt.strftime("%A %d %B %H:%M:%S")
            })
            dt = add_months(dt, cycle_months)

    planning.sort(key=lambda x: x["datetime"])
    return planning


if __name__ == "__main__":
    planning = generate_planning(planning_rules)
    print(json.dumps(planning, indent=2, ensure_ascii=False))
