
# Define the team members and their respective team numbers
team_data = {
    "Mika": 1, "Maria": 1, "Isis": 1, "Rosa": 1, "Maja": 1, "Damaris": 1,
    "Emily": 2, "Celia": 2, "Carine": 2, "Sabrina": 2, "Maria": 2, "Gur": 2,
    "Elisa": 3, "Sari": 3, "Dave": 3, "Dima": 3, "Jesper": 3, "Martyna": 3,
    "Kelt": 4, "Sebastian": 4, "Quanpu": 4, "Ruben": 4, "Sofia": 4, "Gabriella": 4,
    "Kian": 5, "Sahir": 5, "Tom": 5, "Gonzalo": 5, "Ameer": 5, "Teun": 5,
    "Angelica": 6, "Matas": 6, "Caleb": 6, "Angeline": 6, "Raven": 6, "Paulina": 6,
    "Martyna": 7, "Maja": 7, "Mate": 7, "Vincent": 7, "Eryk": 7, "Emma": 7,
    "Hielke": 8, "Liss": 8, "Beatris": 8, "Caio": 8, "Sally": 8, "Sanne": 8,
    "Atlas": 9, "Elli": 9, "Felix": 9, "Diana": 9, "Yash": 9,
    "Akanksha": 10, "Charlie": 10, "Andrey": 10, "Max": 10, "Hugo": 10, "Al-fatihi": 10,
    "Misha": 11, "Ioanna": 11, "Ella": 11, "Cristian": 11, "Alicja": 11, "Vanessa": 11,
    "Luca": 12, "Rachna": 12, "Jelle": 12, "Karolina": 12, "Yuyue": 12, "Alexia": 12
}

# Function to find the team number for a given member name
def solution_station_5(input):
    return team_data.get(input, "Member not found in any team")

# Example usage
input_name = input("Enter a member name:")  # Replace with the name you want to look up
team_number = solution_station_5(input_name)

if team_number != "Member not found in any team":
    print(f"{input_name} is in Team {team_number}")
else:
    print(team_number)
