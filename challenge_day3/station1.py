def solution_station_1(n): 

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return solution_station_1(n-1)+solution_station_1(n-2)

