import re

from dateutil import parser
from fastapi import HTTPException


def normalize_date(date_str: str):
    date_str = re.sub(r'\bгода?\b', '', date_str).strip()

    try:
        date = parser.parse(date_str, dayfirst=True, fuzzy=True)
        return date.strftime("%d.%m.%Y")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")


def normalize_duration(duration_str: str) -> str:
    years, months, weeks, days = 0, 0, 0, 0
    duration_str = duration_str.lower()

    year_match = re.search(r'(\d+)\s*(год|лет)', duration_str)
    if year_match:
        years = int(year_match.group(1))

    month_match = re.search(r'(\d+)\s*месяц', duration_str)
    if month_match:
        months = int(month_match.group(1))

    week_match = re.search(r'(\d+)\s*недел', duration_str)
    if week_match:
        weeks = int(week_match.group(1))

    day_match = re.search(r'(\d+)\s*дн', duration_str)
    if day_match:
        days = int(day_match.group(1))

    print(f'{years}_{months}_{weeks}_{days}')

    return f'{years}_{months}_{weeks}_{days}'
