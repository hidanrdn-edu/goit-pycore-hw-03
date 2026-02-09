# Task 1 
import datetime

def get_days_from_today(date):  # date format - 'YYYY-MM-DD' 
    try:
        today = datetime.date.today()
        input_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        delta = today - input_date
        return int(delta.days)
    except ValueError:
        return f"Помилка: неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'."
    except TypeError:
        return "Помилка: дата має бути рядком (строка)"
    except Exception as e:
        return f"Непередбачена помилка: {e}"


print(get_days_from_today("2026-02-01"))

