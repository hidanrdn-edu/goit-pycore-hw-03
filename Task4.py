#Task 4
from datetime import datetime, date, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user.get('birthday', ''), '%Y.%m.%d').date()
        birthday_this_year = date(today.year, birthday.month, birthday.day)


        if birthday_this_year < today:
            birthday_this_year = date(today.year + 1, birthday.month, birthday.day)


        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            cong_date = birthday_this_year
            if cong_date.weekday() >= 5:
                shift = 7 - cong_date.weekday()
                cong_date = cong_date + timedelta(days=shift)

            result.append({
                'name': user.get('name', ''),
                'congratulation_date': cong_date.strftime('%Y.%m.%d')
            })

    return result


users = [
    {'name': 'John Doe', 'birthday': '1985.02.08'},
    {'name': 'Jane Smith', 'birthday': '1990.02.11'},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print('Список привітань на цьому тижні:', upcoming_birthdays)
