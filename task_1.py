from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    birthdays_by_day = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if today <= birthday_this_year <= today + timedelta(days=6):
            birthday_day = birthday_this_year.strftime("%A")

            if birthday_day in ["Saturday", "Sunday"]:
                birthday_day = "Monday"
            birthdays_by_day[birthday_day].append(name)

    for day, names in birthdays_by_day.items():
        print(f"{day}: {', '.join(names)}")


users = [
    {"name": "Anna True", "birthday": datetime(1976, 10, 29)},
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Bear Koum", "birthday": datetime(1976, 10, 27)},
    {"name": "Liza Pest", "birthday": datetime(1976, 10, 26)},
    {"name": "Void Kall", "birthday": datetime(1976, 10, 25)},
    {"name": "Spirit Vestr", "birthday": datetime(1976, 10, 24)},
    {"name": "Gus Bust", "birthday": datetime(1976, 10, 23)},
    {"name": "Jan Cloud", "birthday": datetime(1976, 10, 22)},
]

get_birthdays_per_week(users)
