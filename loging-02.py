import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('app.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

class Log:
    def info(self):
        logger.info("This is an information about something.")

    def error(self):
        logger.error("We can't divide any numbers by zero.")

    def warning(self):
        logger.warning("Insufficient funds.")

    def debug(self):
        logger.debug("This is debug message.")

    def critical(self):
        logger.critical("Medic!! We've got critical damages.")


log = Log()
log.info()
log.error()
log.warning()
log.debug()
log.critical()
