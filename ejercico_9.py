from datetime import date, timedelta

def count_mondays(birthday: date, current_date: date) -> int:
    age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))
    working_years = min(78, age) - 22
    start_date = birthday + timedelta(days=(22*365))
    end_date = start_date + timedelta(days=(working_years*365))
    mondays = 0
    current_weekday = start_date
    while current_weekday <= end_date:
        if current_weekday.weekday() == 0:
            mondays += 1
        current_weekday += timedelta(days=1)
    return mondays

if __name__ == "__main__":
    birthday = date(1998, 7, 15)
    current_date = date(2022, 1, 10)
    mondays = count_mondays(birthday, current_date)
    print("Número de lunes:", mondays)