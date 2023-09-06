def solution_station_4(input):
    if (input == 1):
        return False
    else:
        for i in range(2, input):
            if input % i == 0:
                return False  
        return True  

