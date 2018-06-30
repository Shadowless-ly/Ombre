import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                    datefmt="%a, %d %b %Y %H:%M:%S",
                    stream=sys.stdout
                            )

logging.info("info message")
logging.debug("debug message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
