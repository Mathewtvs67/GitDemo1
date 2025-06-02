import inspect
import logging

class BaseClass:
    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        filehandler=logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s:  %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatter)
        logger=logging.getLogger(loggerName)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
