#-*- coding:utf-8 -*-

import csv

def csv_write(file, data_list):
    with open(file, "a+") as f:
        f_csv = csv.writer(f, dialect='excel')
        f_csv.writerow(data_list)