
# payroll_writer.py by Chufan Wu
# Dec. 2021

import openpyxl
import payroll_logger

def excel_initializer(): 
    payroll_logger.log_printer("i", "Excel file initialization started. ")
    wb = openpyxl.Workbook()

    ws_1 = wb.active

def data_validation(list): 

    return True

def excel_writer(file): 
    wb = openpyxl.Workbook()

    ws_1 = wb.active
