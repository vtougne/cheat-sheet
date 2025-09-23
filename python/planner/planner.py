#!/usr/bin/env python3
import argparse
import json
import yaml
import re
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

# France timezone
TZ_PARIS = ZoneInfo("Europe/Paris")

# Input: English rules with hour and cycle
planning_rules = {
    "patch_app1": {"rule": "3rd Tuesday March 2025", "hour": "02:00", "cycle": "3 months"},
    "patch_app2": {"rule": "2nd Thursday June 2025", "hour": "04:30", "cycle": "6 months"},
    "patch_app3": {"rule": "1st Monday September 2025", "hour": "01:15", "cycle": "12 months"}
}

# Generation duration
YEARS_TO_GENERATE = 2

# Lookup tables
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
    """Extracts nth day, weekday, month and year from the rule."""
    match = re.match(r"(\d+)(st|nd|rd|th)\s+(\w+)\s+(\w+)\s+(\d{4})", rule_str.strip(), re.IGNORECASE)
    if not match:
        raise ValueError(f"Invalid rule format: {rule_str}")
    week_num = int(match.group(1))
    weekday = WEEKDAY_TO_INDEX[match.group(3).lower()]
    month = MONTH_TO_INDEX[match.group(4).lower()]
    year = int(match.group(5))
    return week_num, weekday, month, year


def nth_weekday(year, month, weekday, n):
    """Returns the date of the nth `weekday` in a given month."""
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
    """Adds months to a date."""
    year = orig_date.year + (orig_date.month + months - 1) // 12
    month = (orig_date.month + months - 1) % 12 + 1
    
    # Try to keep the original day, handle end of month cases
    day = orig_date.day
    try:
        return orig_date.replace(year=year, month=month, day=day)
    except ValueError:
        # If day doesn't exist in target month, use last day of month
        import calendar
        day = calendar.monthrange(year, month)[1]
        return orig_date.replace(year=year, month=month, day=day)


def generate_planning(rules, years=2):
    """Generates the planning for the provided rules."""
    planning = []
    now = datetime.now()
    max_date = now.astimezone(TZ_PARIS).replace(year=now.year + years)

    for app, data in rules.items():
        # Handle both old format (single rule) and new format (multiple rules)
        if "rule" in data:
            # Old format - single rule
            rule_list = [{"start": data["rule"], "hour": data.get("hour", "00:00"), "cycle": data.get("cycle", "3 months")}]
        elif "rules" in data:
            # New format - multiple rules
            rule_list = data["rules"]
        else:
            continue
            
        # Process each rule for this app
        for rule_data in rule_list:
            start_rule = rule_data["start"]
            hour_str = rule_data.get("hour", "00:00")
            cycle_str = rule_data.get("cycle", "3 months")

            n, weekday, month, year = parse_rule(start_rule)
            
            # Handle string, numeric, and time object hour formats
            if isinstance(hour_str, str):
                hour, minute = map(int, hour_str.split(":"))
            elif isinstance(hour_str, time):
                # YAML parser converted "13:00" to a time object
                hour, minute = hour_str.hour, hour_str.minute
            elif isinstance(hour_str, int):
                # YAML parser converted "13:00" to minutes (780 = 13*60)
                # Convert back to hours and minutes
                hour = hour_str // 60
                minute = hour_str % 60
            else:
                # Default fallback
                hour, minute = 0, 0

            # Extract number of months from cycle
            match = re.match(r"(\d+)\s+months", cycle_str.strip(), re.IGNORECASE)
            cycle_months = int(match.group(1)) if match else 3

            # Generation
            current_year = year
            current_month = month
            
            while True:
                # Recalculate the nth weekday for the current month/year
                target_date = nth_weekday(current_year, current_month, weekday, n)
                if not target_date:
                    break
                    
                # Create datetime at midnight, then add the specified hour
                dt = datetime.combine(target_date, time(0, 0)).replace(tzinfo=TZ_PARIS)
                dt = dt.replace(hour=hour, minute=minute)
                
                if dt > max_date:
                    break
                    
                entry = {
                    "app": app,
                    "datetime": dt.strftime("%A %d %B %Y %H:%M:%S"),
                    "_sort_key": dt  # Add datetime object for proper sorting
                }
                
                # Include meta data if present
                if "meta" in data:
                    entry["meta"] = data["meta"]
                
                planning.append(entry)
                
                # Move to the next cycle
                next_month = current_month + cycle_months
                current_year += (next_month - 1) // 12
                current_month = (next_month - 1) % 12 + 1

    # Sort by actual datetime object, then remove the sort key
    planning.sort(key=lambda x: x["_sort_key"])
    for entry in planning:
        del entry["_sort_key"]
    return planning


def load_planning_rules(input_file):
    """Load planning rules from a YAML or JSON file."""
    with open(input_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data.get('planning_rules', data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate scheduling planner based on rules')
    parser.add_argument('-i', '--input', 
                        help='Input YAML or JSON file containing planning rules', 
                        default=None)
    
    args = parser.parse_args()
    
    if args.input:
        rules = load_planning_rules(args.input)
    else:
        rules = planning_rules
    
    planning = generate_planning(rules)
    print(json.dumps(planning, indent=2, ensure_ascii=False))
