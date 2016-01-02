"""
Simple logger for sentinal

Author: petersonb
"""

def log(source, logtype, message):
    logfile = open("log","a")
    logfile.write("{0} {1} : {2}\n".format(source, logtype, message.strip()))
    logfile.close()

def debug(source, message):
    log(source, "DEBUG", message)
