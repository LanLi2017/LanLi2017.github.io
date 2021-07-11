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


if __name__ == "__main__":
    main()
