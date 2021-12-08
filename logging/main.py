import logging
import datetime as dt

# Logging Levels: 
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

today = dt.datetime.today()
filename = f"{today.month:02d}_{today.day:02d}_{today.year}"

logging.basicConfig(level=logging.DEBUG)

# for handler in logging.root.handlers:
#     logging.root.removeHandler(handler)

logger = logging.getLogger("PythonLogger")

try:
    pass

except:
    logger.error(DEBUG)

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("This is DEBUG")
logger.info("This is Info")
logger.warning("This is Warning")


