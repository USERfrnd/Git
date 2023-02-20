import inspect
import logging


class BaseClass:
    def test_loggingDemo(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("logfileSS.log")
        logger.addHandler(fileHandler)

        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger
