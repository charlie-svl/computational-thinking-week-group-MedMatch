# -- coding: utf-8 --
import datetime
def solution_station_2(input):
        
        year, month, day = map(int, input.split('-'))

        date_obj = datetime.datetime(year, month, day)
        day_of_week = date_obj.weekday()

        weekdays = {
        0: "月曜日",
        1: "火曜日",
        2: "水曜日",
        3: "木曜日",
        4: "金曜日",
        5: "土曜日",
        6: "日曜日"
        }
        
        weekday = weekdays[day_of_week]
        return weekday