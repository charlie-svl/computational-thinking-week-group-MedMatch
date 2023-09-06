import datetime
def solution_station_1(input):
        
        year, month, day = map(int, input.split('-'))

        date_obj = datetime.datetime(day, month, year)
        day_of_week = date_obj.weekday()

        weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
        }
        
        weekday = weekdays[day_of_week]
        print("The day of the week for", input, "is", weekday)
        return

solution_station_1("17-04-2023")


        