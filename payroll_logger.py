
# payroll_logger.py by Chufan Wu
# Dec. 2021

import datetime

# return current time stamp for log recording
def timestamp_ms(): 
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

# print log content
def log_printer(level, content, file = "./payroll/ApplicationOut.log"):

    # create the list includes log levels
    log_file = open(file, mode = "a")

    # log tag
    if level == "f": 
        log_level = " [FATAL] "
    
    elif level == "e": 
        log_level = " [ERROR] "

    elif level == "w": 
        log_level = " [WARN] "
    
    elif level == "i": 
        log_level = " [INFO] "
    
    elif level == "d": 
        log_level = " [DEBUG] "
    
    elif level == "t": 
        log_level = " [TRACE] "
    
    else: 
        log_level = " [UNDEFINED] "
    
    # print log content to stdout
    log_content = timestamp_ms() + log_level + content
    print(log_content)

    # print log content to log file
    log_file.write(log_content + "\n")
    log_file.close()
