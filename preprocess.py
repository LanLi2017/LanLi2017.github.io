import csv
import json
from csv import DictReader
from pprint import pprint

import pandas as pd


def transpose(csv_p, out_p):
    data = []
    with open(csv_p, 'rt', encoding='utf-8', newline='')as f:
        for row in DictReader(f):
            # Province/States,Country/Region,WHO region,WHO region label,
            prov = row.pop('Province/States')
            country = row.pop('Country/Region')
            who_reg = row.pop('WHO region')
            who_label = row.pop('WHO region label')
            for date, value in row.items():
                data.append({
                    'Province/states': prov,
                    'country': country,
                    'WHO region': who_reg,
                    'WHO region label': who_label,
                    'date': date,
                    'value': value,
                })

    # out_file = open("dataset/who_covid_19_china_transpose.json", "w")
    #
    # json.dump(data, out_file, indent=4)
    #
    # out_file.close()
    keys = data[0].keys()
    with open(out_p, 'w', newline='')as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


def main():
    countries = ['China', 'Germany', 'haiti', 'Turkey', 'US']
    for country in countries:
        csv_p = f'dataset/who_covid_19_{country}.csv'
        out_p = f'transpose_ds/who_covid_19_{country}_transpose.csv'
        transpose(csv_p, out_p)


def match_code():
    csv_1 = 'dataset/world_map_cases.csv'
    csv_2 = 'dataset/pop.csv'
    csv_3 = 'dataset/world_cases_process.csv'
    with open(csv_1, 'r')as f1, open(csv_2, 'r') as f2, open(csv_3, 'w')as f3:
        writer = csv.writer(f3)
        all = []
        reader1 = csv.reader(f1)
        row = next(reader1)
        row.append('code')
        row.remove('date')
        all.append(row)
        reader2 = csv.reader(f2)
        next(reader2)
        list1 = list(reader1)
        list2 = list(reader2)
        for row1 in list1:
            country_name = row1[0]
            count = row1[2]
            flag = False
            for row2 in list2:
                name = row2[0]
                code = row2[1]
                if name == country_name:
                    all.append([country_name, count, code])
                    flag = True
                    break
            if not flag:
                all.append([country_name, count, ''])

        writer.writerows(all)


def India_data():
    csv_p = 'dataset/who_covid_19_India.csv'
    out_p = 'transpose_ds/who_covid_19_India_transpose.csv'
    transpose(csv_p, out_p)


if __name__ == "__main__":
    India_data()
    # match_code()
    # main()
