import re
import csv

def read_province_file_by_id(path):
    province_file = open(path)
    province_file_reader = csv.reader(province_file, delimiter=';')

    provinces = {}
    for row in province_file_reader:
        if row[0].startswith('PROV'):
            province_name = row[1] # Just pick the 2nd column as name
            province_id = int(row[0][4:])
            provinces[province_id] = province_name.lower()

    province_file.close()
    return provinces

def read_province_file_by_name(path):
    province_file = open(path)
    province_file_reader = csv.reader(province_file, delimiter=';')

    provinces = {}
    for row in province_file_reader:
        if row[0].startswith('PROV'):
            province_name = row[1].lower() # Just pick the 2nd column as name
            province_id = int(row[0][4:])
            provinces[province_name] = province_id

    province_file.close()
    return provinces
