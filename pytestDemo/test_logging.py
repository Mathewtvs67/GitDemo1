import logging

def test_loggingDemo():
    filehandler=logging.FileHandler('logfile.log')
    formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    filehandler.setFormatter(formatter)
    logger=logging.getLogger(__name__)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    logger.info("Information statement")
    logger.debug('debug statement')
    logger.error('error statement')
    logger.critical('critical statement')