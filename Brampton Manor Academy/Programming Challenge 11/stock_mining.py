import csv
from pathlib import Path


def check_file_exists(path):
    return path.is_file()


def read_csv(csv_path):
    csv_array = []
    if check_file_exists(csv_path):
        with open(csv_path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                csv_array.append(row)
    return csv_array


def data_splitter(csv):
    monthly_dictionary = {}
    processed_month_list = []

    for row in csv:
        date = row[0].split('-')
        year_month = date[0] + '-' + date[1]

        if year_month not in processed_month_list:
            monthly_dictionary[year_month] = [[], [], []]
            processed_month_list.append(year_month)

        if year_month == (row[0])[:-3]:
            monthly_dictionary[year_month][0] = float(row[5])
            monthly_dictionary[year_month][1] = float(row[6])
            monthly_dictionary[year_month][2] = float(row[5]) * float(row[6])

    sorted_dict = list(sorted(monthly_dictionary.items(), reverse=True, key=lambda x: x[1]))
    return sorted_dict


def output(monthly_dictionary):
    print('The best 6 months are:')
    for count in range(6):
        print(monthly_dictionary[count][0])

    print('\nThe worst 6 months are:')
    for count in range(6):
        print(monthly_dictionary[::-1][count][0])


if __name__ == '__main__':
    csv_path = Path('AAPL.csv')
    csv_array = read_csv(csv_path)
    monthly_dictionary = data_splitter(csv_array)
    output(monthly_dictionary)
