import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler("logfile.log")
    logger.addHandler(fileHandler)

    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
    fileHandler.setFormatter(formatter)
    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is done")
    logger.info("Information statement")
    logger.warning("Warning mode")
    logger.error("Issue occurred")
    logger.critical("critical issue")

