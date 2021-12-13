
# payroll.py by Chufan Wu
# Dec. 2021

import os
import payroll_loader
import payroll_logger

csv_records = []
csv_files = []
excel_file = "payroll.xlsx"

payroll_logger.log_printer("i", "Process started. ")

# get current work directory
current_work_path = os.getcwd()
payroll_logger.log_printer("i", "Current work path is: " + current_work_path)

# find all csv files in the directory and add to the file list
for file in os.listdir("./payroll"): 
    if not file.endswith(".csv"): 
        continue
    csv_files.append(file)
    payroll_logger.log_printer("i", str(file) + " has been successfully scaned. ")

payroll_logger.log_printer("d", str(csv_files))
csv_files.sort()
payroll_logger.log_printer("d", str(csv_files))

# load each csv file and write to excel file
for csv_file in csv_files:
    csv_records.append(payroll_loader.csv_loader("./payroll/" + str(csv_file)))
    payroll_logger.log_printer("i", str(csv_file) + " has been successfully loaded. ")
    payroll_logger.log_printer("d", str(csv_records))

payroll_logger.log_printer("i", "Process finished. ")
