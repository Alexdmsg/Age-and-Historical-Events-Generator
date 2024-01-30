# project.py
from datetime import date, datetime
from historical_events import historical_events

def main():
    birth_day = input("Enter the day of your birth (2 digits): ")
    birth_month = input("Enter the month of your birth (2 digits): ")
    birth_year = input("Enter the year of your birth (4 digits): ")

    try:
        birth_date = validate_date_input(birth_day, birth_month, birth_year)
        today = date.today()
        age = calculate_age(birth_date, today)

        print(f"Your age as of {today.strftime('%B %d, %Y')} is {age}.")

        # Get historical events for the birth year
        events_for_birth_year = historical_events.get(birth_date.year, "No historical events found for this year.")
        print(f"\nHistorical Events in {birth_date.year}:\n{events_for_birth_year}")

    except ValueError as e:
        print(f"Error: {e}")

def validate_date_input(day, month, year):
    try:
        return datetime.strptime(f"{month}-{day}-{year}", "%m-%d-%Y").date()
    except ValueError:
        raise ValueError("Invalid date input. Please check the day, month, and year.")

def calculate_age(birth_date, today):
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day

    if age_days < 0:
        last_month = today.replace(month=today.month - 1)
        days_in_last_month = (today - last_month).days
        age_days += days_in_last_month
        age_months -= 1

    if age_months < 0:
        age_months += 12
        age_years -= 1

    return f"{age_years} years, {age_months} months, and {age_days} days"

if __name__ == "__main__":
    main()
