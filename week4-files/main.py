import json
import csv


csv_file = open('test.csv')
csv_reader = csv.reader(csv_file)
for row in csv_reader:
    print(row)
csv_file.close()



file_reader = open("test.txt")

contents = file_reader.readlines()

file_reader.close()

for index in range(len(contents)):
    print(f'Line #{index+1}: {contents[index]}', end='')

# truncate the file if it exists, or create it
file_writer = open("output.wednesday", 'w')

file_writer.write("happy wednesday\n")
file_writer.write("are we done yet?\n")

file_writer.close()


# bing - python json read and write exam
# Python dictionary
data = {
"name": "Alice",
"age": 28,
"skills": ["Python", "Data Analysis", "Machine Learning"]
}

# Write JSON to file
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4) # indent for pretty formatting


with open('data.json') as json_file_to_read:
    data_from_file = json.load(json_file_to_read)

print(data_from_file)

foods = ['pizza', 'pasta', 'burgers', 'tacos']
with open("foods.json", "w", encoding="utf-8") as file:
    json.dump(foods, file, indent=4) # indent for pretty formatting

# bing and umgpt - python csv
csv_file = open('foods.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
for food in foods:
    csv_writer.writerow([food])
csv_file.close()