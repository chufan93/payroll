
# payroll_loader.py by Chufan Wu
# Dec. 2021

import csv
import payroll_logger

def csv_loader(file): 
    # create an empty list to store payroll data
    records = []

    # open payroll csv file
    payroll_file = open(file, mode = "r")
    payroll_logger.log_printer("i", str(file) + " has been successfully opened. ")

    payroll_reader = csv.reader(payroll_file)
    payroll_logger.log_printer("i", str(file) + " has been successfully read. ")

    # read lines into list
    for row in payroll_reader: 
        records.append(row)
    
    payroll_logger.log_printer("i", str(file) + " has been successfully loaded into list. ")
    payroll_logger.log_printer("d", str(records))

    # close csv file after loading process
    payroll_file.close()
    payroll_logger.log_printer("i", str(file) + " has been successfully closed. ")

    return records
