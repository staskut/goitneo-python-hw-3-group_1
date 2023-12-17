from collections import defaultdict
from datetime import datetime


def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days



        if delta_days < 7:
            birthday_day = birthday_this_year.weekday()
            if birthday_day in [5, 6]:
                birthday_day = 0

            weekday_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            birthdays[weekday_name[birthday_day]].append(name)




    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")





if __name__=="__main__":
    users_example = [
        {"name": "Bill Gates", "birthday": datetime(1955, 12, 7)},
        {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
        {"name": "Jill Valentine", "birthday": datetime.today()},
        {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)}
    ]

    get_birthdays_per_week(users_example)
