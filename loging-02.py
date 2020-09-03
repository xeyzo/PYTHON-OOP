import logging

logger = logging.getLogger("logging_tryout2")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s","%Y-%m-%d %H:%M:%S")

ch.setFormatter(formatter)

logger.addHandler(ch)

logger.error("We can't divide any numbers by zero.")
logger.info("This is an information about something.")
# logger.notice("Someone loves your status.")
logger.warning("Insufficient funds.")
logger.debug("This is debug message.")
# logger.alert("Achtung! Achtung!")
# logger.critical("Medic!! We've got critical damages.")
# logger.emergency("System hung. Contact system administrator immediately!")