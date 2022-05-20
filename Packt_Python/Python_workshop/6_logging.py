# Logging
#Levels of log alerts: lowest:debug => highest:fatal
import logging
logger = logging.getLogger("logger_name")
logger.debug("Logging at debug")
logger.info("Logging at info")
logger.warning("Logging at warning")
logger.error("Logging at error")
logger.fatal("Logging at fatal")
system = 'Moon'
for number in range(3):
    logger.warning("%d errors reported in %s", number, system)
try:
    int("nope")
except Exception:
    logging.error("Something bad happened", exc_info=True)
try:
    int("nope")
except Exception:
    logging.exception("Something bad happened")

#Preferences (for linters)
import logging
logging.info("string template %s", variable)            ##Better
logging.info("string template {}".format(variable))
d = dict()
try:
    d["missing_key"] += 1
except Exception:
    logging.error("Something bad happened", exc_info=True)  #Better
try:
    d["missing_key"] += 1
except Exception as e:
    logging.error("Something bad happened: %s", e)

import logging
import sys
root_logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(levelname)s: %(message)s")
handler.setFormatter(formatter)
root_logger.addHandler(handler)
root_logger.setLevel("INFO")
logging.info("Hello logger world")

#restart kernel
#
import logging
from logging.config import dictConfig
dictConfig({
    "version": 1,
    "formatters": {
        "short": {
            "format": "%(levelname)s: %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "short",
            "stream": "ext://sys.stdout",
            "level": "DEBUG"
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO"
        }
    }
})
logging.info("Hello logging world")

#restart kernel
#
import sys
import logging
logging.basicConfig(
    level = "INFO",
    format = "%(levelname)s: %(message)s",
    stream = sys.stdout
)
logging.info("Hello logging world")

import logging
from logging.config import fileConfig
fileConfig("logging_config.ini")
logging.info("hello there")