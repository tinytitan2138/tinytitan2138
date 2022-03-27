import logging
logger = logging.getLogger(__name__)
logger.info('Hello from helper')
logger2 = logging.getLogger(__name__)
stream_h = logging.StreamHandler()  # Create handler
file_h = logging.FileHandler('file.log')
# Level and the format
stream_h.setLevel(logging.WARNING)
file_h.setlevel(logging.ERROR)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a warning")
logger.error('this is an error')

