import datetime
def solution_station_1(input):
        year, month, day = map(int, input.split('-'))

        # Create a datetime object without using the date() constructor
        date_obj = datetime.datetime(year, month, day)

        # Get the day of the week as an integer (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
        day_of_week = date_obj.weekday()

        # Define a list of weekday names
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Print the day of the week
        print(f"The day of the week for {date_str} is {weekdays[day_of_week]}")
        return

solution_station_1(17-04-2023)


        