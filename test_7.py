import csv
import random
import string

def generate_random_data(N, header):
    value = 0
    data = []
    for _ in range(N):
        row = {}
        for column, data_type in header.items():
            if data_type == 'int':
                value = random.randint(0, 100)
            elif data_type == 'str':
                value = ''.join(random.choices(string.ascii_letters, k=random.randint(1, 100)))
            elif data_type == 'bool':
                value = random.choice([True, False])
            row[column] = value
        data.append(row)
    return data


def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data[0].keys())

        for row in data:
            writer.writerow(row.values())

header = {'Column1': 'int', 'Column2': 'str', 'Column3': 'bool'}
N = 10

random_data = generate_random_data(N, header)
print(random_data)
save_to_csv(random_data, 'random_data.csv')
