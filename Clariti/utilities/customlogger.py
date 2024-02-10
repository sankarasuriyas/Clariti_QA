import logging
class LogGen:
    LOG_FILE = '.\\Logs\\automation.log'
    # using parallel runs -n=2, clear logs will not work due to same file accessing for multiple node.
    #@staticmethod
    #def clear_logs():
    #    if os.path.exists(LogGen.LOG_FILE):
    #        os.remove(LogGen.LOG_FILE)
    @staticmethod
    def loggen():
        #LogGen.clear_logs()
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=LogGen.LOG_FILE,mode='a')
        #formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
