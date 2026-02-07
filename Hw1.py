# Task 1 
import datetime

def get_days_from_today(date):  # date format - 'YYYY-MM-DD' 
    today = datetime.date.today()
    input_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    delta = today - input_date
    return int(delta.days)

#print(get_days_from_today("2026-02-01")) 

# Task 2
import random
import re

def get_numbers_ticket(min, max, quantity): #min > 1, max < 1000 
    if min < 1 or max > 1000 or min >= max or quantity > (max - min + 1):
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    return sorted(numbers)

#print(get_numbers_ticket(1, 100, 5))

# Task 3
def normalize_phone(phone_number):
    if not isinstance(phone_number, str):
        phone_number = '' if phone_number is None else str(phone_number)

    cleaned = phone_number.strip()
    has_plus = cleaned.startswith('+')
    digits = re.sub(r"\D", "", cleaned)

    if not digits:
        return ''

    if has_plus:
        return '+' + digits

    if digits.startswith('380'):
        return '+' + digits

    return '+38' + digits

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
#print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

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

