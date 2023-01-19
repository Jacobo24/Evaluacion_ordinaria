#Si contamos todos los lunes que ha vivido una persona "esos lunes malos y buenos"
import datetime

def number_of_mondays(birthday, current_date):
    age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))
    if age < 22 or age > 78:
        return 0
    days_between_dates = (current_date - birthday).days
    number_of_mondays = days_between_dates // 7
    return number_of_mondays

if __name__ == '__main__':
    birthday = datetime.date(1998, 7, 15)
    current_date = datetime.date(2022, 1, 10)
    mondays = number_of_mondays(birthday, current_date)
    print(mondays)