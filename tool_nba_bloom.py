import json

json_filename = "nba_stats.json"
output_filename = "nba_stats_with_text.json"

with open(json_filename, 'r') as jsonfile:
    data = json.load(jsonfile)

json_data_with_text = []
for row in data:
    player_name = row["prompt"].split(":")[0].strip()
    text = f"Instruction:\nGive me the statistics of the player {player_name}\n\n### Response:\n{row['completion']}"
    row["text"] = text
    json_data_with_text.append(row)

with open(output_filename, 'w') as outfile:
    json.dump(json_data_with_text, outfile, indent=4)
