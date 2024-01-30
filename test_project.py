# test_project.py
import unittest
from unittest.mock import patch
from io import StringIO
from datetime import date, timedelta
from project import main, validate_date_input, calculate_age, historical_events

class TestProject(unittest.TestCase):
    def test_main_function(self):
        for year in range(1822, 2022):
            with self.subTest(year=year):
                input_data = [
                    str(date.today().day).zfill(2),
                    str(date.today().month).zfill(2),
                    str(year)
                ]
                with patch("builtins.input", side_effect=input_data), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                    main()
                    output = mock_stdout.getvalue().strip()

                # Check age calculation
                expected_age_output = f"Your age as of {date.today().strftime('%B %d, %Y')} is {date.today().year - year} years, 0 months, and 0 days."
                self.assertIn(expected_age_output, output)

                # Check historical events using the dictionary
                events_for_birth_year = historical_events.get(year, "No historical events found for this year.")
                expected_events_output = f"Historical Events in {year}:\n{events_for_birth_year}"
                self.assertIn(expected_events_output, output)

    def test_validate_date_input_valid_date(self):
        # Test validate_date_input with a valid date
        result = validate_date_input("01", "01", "2000")
        expected_result = date(2000, 1, 1)
        self.assertEqual(result, expected_result)

    def test_validate_date_input_invalid_date(self):
        # Test validate_date_input with an invalid date
        with self.assertRaises(ValueError):
            validate_date_input("32", "13", "2022")

    def test_calculate_age_same_date(self):
        # Test calculate_age when birth date is the same as today
        birth_date = date.today()
        result = calculate_age(birth_date, birth_date)
        expected_result = "0 years, 0 months, and 0 days"
        self.assertEqual(result, expected_result)

    def test_calculate_age_future_date(self):
        # Test calculate_age when birth date is in the future
        birth_date = date.today() + timedelta(days=1)
        with self.assertRaises(ValueError):
            calculate_age(birth_date, date.today())

    def test_historical_events_for_birth_year(self):
        # Test historical events for a specific birth year
        birth_year = 2000
        events_for_birth_year = historical_events.get(birth_year, "No historical events found for this year.")
        expected_result = "Y2K fears; Sydney hosts the Summer Olympics."
        self.assertEqual(events_for_birth_year, expected_result)

    # Add more test cases for historical_events module based on different scenarios

if __name__ == "__main__":
    unittest.main()
