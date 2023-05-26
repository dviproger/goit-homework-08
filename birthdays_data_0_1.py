from datetime import datetime,  date

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
    {'name': 'Voldemar', 'birthday': date(year=1982, month=1, day=13)},
    {'name': 'Mike', 'birthday': date(year=1986, month=2, day=2)},
    {'name': 'Jil', 'birthday': date(year=1967, month=6, day=1)},
    {'name': 'Ann', 'birthday': date(year=1978, month=4, day=11)},
    {'name': 'Mery', 'birthday': date(year=1988, month=5, day=30)},
    {'name': 'Krees', 'birthday': date(year=1998, month=6, day=2)},
    {'name': 'Rob', 'birthday': date(year=1956, month=5, day=30)},
    {'name': 'Will', 'birthday': date(year=1966, month=8, day=12)},
    {'name': 'Den', 'birthday': date(year=1987, month=9, day=17)},
    {'name': 'Koop', 'birthday': date(year=1980, month=10, day=18)},
    {'name': 'Rex', 'birthday': date(year=1989, month=11, day=19)},
    {'name': 'Fedor', 'birthday': date(year=1959, month=12, day=4)},
    {'name': 'Julia', 'birthday': date(year=1992, month=11, day=8)},
    {'name': 'Bon', 'birthday': date(year=1934, month=10, day=10)},
    {'name': 'Jaims', 'birthday': date(year=1976, month=9, day=21)},
    {'name': 'Kameron', 'birthday': date(year=1990, month=8, day=14)},
    {'name': 'Kirk', 'birthday': date(year=1970, month=5, day=25)},
    {'name': 'Don', 'birthday': date(year=1996, month=5, day=25)},
    {'name': 'Jan', 'birthday': date(year=1996, month=5, day=26)},
    {'name': 'Arny', 'birthday': date(year=1984, month=5, day=29)}
]

# Обьявим переменные для накопления выборки за неделю.
carrent_date = datetime.today().date()
carent_weekday = carrent_date.weekday()
print(carrent_date, carrent_date.weekday())
end_week = 6 - carent_weekday
result_dict = {}
result_list_next_week = []
for i in range(6):
    result_dict.update({i: []})


# Функция находит именинников из списка сотрудников на неделю вперед до конца недели.
def get_birthdays_per_week(data_users):
    if not data_users:
        print('No data for serch')
        exit()
    else:
        for user in data_users:
            ub = user['birthday']
            if carrent_date.month == ub.month and (carrent_date.day <= ub.day <= (carrent_date.day + end_week)):
                if ub.weekday() != 6:
                    result_dict[ub.weekday()].append(user['name'])
                else:
                    result_list_next_week.append(user['name'])

        for key, value in result_dict.items():
            if value:
                print(f'{days_name[key]} :  {", ".join(value)}')
        if result_list_next_week:
            print(f'Next week Mondey : {", ".join(result_list_next_week)}')


get_birthdays_per_week(users)
