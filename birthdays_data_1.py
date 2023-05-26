from datetime import datetime, date
from collections import defaultdict

days_name = {
    0: "Mondey",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

users = [
    {'name': 'Voldemar', 'birthday': date(1982, 5, 23)},
    {'name': 'Mike', 'birthday': date(1986, 5, 24)},
    {'name': 'Jil', 'birthday': date(1967, 3, 5)},
    {'name': 'Ann', 'birthday': date(1978, 5, 28)},
    {'name': 'Mery', 'birthday': date(1988, 5, 30)},
    {'name': 'Krees', 'birthday': date(1998, 5, 28)},
    {'name': 'Rob', 'birthday': date(1956, 5, 30)},
    {'name': 'Will', 'birthday': date(1966, 5, 27)},
    {'name': 'Den', 'birthday': date(1987, 5, 17)},
    {'name': 'Koop', 'birthday': date(1980, 5, 18)},
    {'name': 'Rex', 'birthday': date(1989, 5, 19)},
    {'name': 'Fedor', 'birthday': date(1959, 6, 2)},
    {'name': 'Julia', 'birthday': date(1992, 5, 8)},
    {'name': 'Bon', 'birthday': date(1934, 5, 10)},
    {'name': 'Jaims', 'birthday': date(1976, 5, 21)},
    {'name': 'Kameron', 'birthday': date(1990, 5, 14)},
    {'name': 'Kirk', 'birthday': date(1970, 5, 27)},
    {'name': 'Don', 'birthday': date(1996, 5, 25)},
    {'name': 'Jan', 'birthday': date(1996, 5, 26)},
    {'name': 'Arny', 'birthday': date(1984, 5, 29)}
]


def get_birthdays_per_week(data_users):
    carrent_date = datetime.today().date()
    carrent_weekday = carrent_date.weekday()
    print('Today is', carrent_date, days_name[carrent_date.weekday()])
    print('-'*30)

    birthdays_carrent_weekday = defaultdict(list)
    birthdays_next_weekday = defaultdict(list)

    for user in data_users:
        ub = user['birthday'].replace(year=carrent_date.year)
        delta_day = (ub - carrent_date).days
        end_week = 6 - carrent_weekday

        if 1 <= delta_day <= 7:

            if 0 <= ub.weekday() <= 5 and delta_day < end_week:
                birthdays_carrent_weekday[ub.weekday()].append(user['name'])

            elif 0 <= ub.weekday() <= 5 and delta_day >= end_week:
                birthdays_next_weekday[ub.weekday()].append(user['name'])

            else:
                birthdays_next_weekday[0].append(user['name'])

    carrent_week_res = sorted(birthdays_carrent_weekday.items())
    next_week_res = sorted(birthdays_next_weekday.items())

    if carrent_week_res:
        print('Birthdays carrent week')
        for i in carrent_week_res:
            print(f'{days_name[i[0]]} :  {", ".join(i[1])}')

    if next_week_res:
        print('Birthdays next week')
        for i in next_week_res:
            print(f'{days_name[i[0]]} :  {", ".join(i[1])}')


def main():
    get_birthdays_per_week(users)


if __name__ == '__main__':
    main()
