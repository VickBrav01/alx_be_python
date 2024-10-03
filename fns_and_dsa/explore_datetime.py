
from datetime import date, datetime, timedelta

def display_current_datetime():
    current_date = datetime.today()
    formated_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formated_date}")
    return current_date

# display_current_datetime()

def future_date():
    add_date = int(input("Enter the number of days to add to the current date: "))
    delta = timedelta(days = add_date)
    future_date = display_current_datetime() + delta
    print(f'Future date: {future_date.strftime("%Y-%m-%d")}')

future_date()











