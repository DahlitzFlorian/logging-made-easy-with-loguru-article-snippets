# customise_format.py
import sys
from loguru import logger

logger.remove(0)
logger.add(sys.stderr, format="<red>{time}</red> <green>{level}</green> {message}", colorize=True)
logger.info("Hello from loguru!")
