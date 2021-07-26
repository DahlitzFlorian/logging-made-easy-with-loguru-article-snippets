# file_logger.py
from loguru import logger

logger.add("normal_file.log")
logger.add("retention_file.log", retention="5 days")
logger.add("rotation_file.log", rotation="1 MB")
logger.add("compress_file.log", compression="zip")

logger.info("Hello from loguru!")
