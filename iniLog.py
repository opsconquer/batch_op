#coding=utf-8
import logging
import datetime

def ini():
    format='%(asctime)s - %(filename)s - %(funcName)s - [line:%(lineno)d] - %(levelname)s - %(message)s'
    curDate = datetime.date.today() - datetime.timedelta(days=0)
    infoLogName =  r'log/info_%s.log' %curDate
    errorLogName =  r'log/error_%s.log' %curDate
     
    formatter = logging.Formatter(format)
     
    infoLogger = logging.getLogger("infoLog")
    errorLogger = logging.getLogger("errorLog")
     
    infoLogger.setLevel(logging.INFO)
    errorLogger.setLevel(logging.ERROR)
     
    infoHandler = logging.FileHandler(infoLogName, 'a')
    infoHandler.setLevel(logging.INFO)
    infoHandler.setFormatter(formatter)
     
    errorHandler = logging.FileHandler(errorLogName, 'a')
    errorHandler.setLevel(logging.ERROR)
    errorHandler.setFormatter(formatter)
     
    infoLogger.addHandler(infoHandler)
    errorLogger.addHandler(errorHandler)

    return infoLogger,errorLogger

if __name__=='__main__':
    infoLogger,errorLogger=ini()
    infoLogger.debug("debug message")
    infoLogger.info("info message")
    infoLogger.warn("warn message")

    errorLogger.error("error message")
    errorLogger.critical("critical message")
