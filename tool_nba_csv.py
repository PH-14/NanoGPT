import csv
import json

csv_file = 'nba_stats.csv'
json_file = 'nba_stats.json'


def generate_summary(row):
    summary = f" {row['Player name']} is a {row['Position']} player for the {row['Team']}. "
    summary += f"At {row['Age']} years old, he has played {row['Games played']} games and averaged {row['Minutes played per game']} minutes per game. "

    field_goals_per_game = float(row['Field goals per game'])
    field_goal_attempts_per_game = float(row['Field goal attempts per game'])
    if field_goal_attempts_per_game != 0:
        field_goal_percentage = (
            field_goals_per_game / field_goal_attempts_per_game) * 100
        summary += f"he has a field goal percentage of {round(field_goal_percentage, 1)}%. "
    else:
        summary += f"he has a field goal percentage of 0%. "

    summary += f"he has an average of {row['Field goals per game']} field goals and attempts {row['Field goal attempts per game']} per game. "
    summary += f"he has made {row['3-point field goals per game']} three-pointers with {row['3-point field goal attempts per game']} attempts. "
    summary += f"In two-point range, he made {row['2-point field goals per game']} shots with {row['2-point field goal attempts per game']} attempts. "
    summary += f"He also contributed with {row['Total rebounds per game']} rebounds, {row['Assists per game']} assists, "
    summary += f"{row['Steals per game']} steals, {row['Blocks per game']} blocks, and commit {row['Turnovers per game']} turnovers per game. "
    summary += f"he has an average of {row['Personal fouls per game']} personal fouls and scores {row['Points per game']} points per game."

    return summary


count = 0  # total is 812 max

# Open the CSV file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file, delimiter=';')

    # Create a list to store the JSON objects
    json_data = []

    # Iterate through each row in the CSV file
    for row in reader:
        prompt = {
            'prompt': f"Generate specific player stats for player: {row['Player name']}:\n",
            'completion': generate_summary(row)
        }
        json_data.append(prompt)

        count += 1
        if count > 400:
            break

# Write the JSON data to a file
with open(json_file, 'w') as file:
    json.dump(json_data, file, indent=4)
