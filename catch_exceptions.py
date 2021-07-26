# catch_exceptions.py
from loguru import logger


@logger.catch
def division(divident: int, divisor: int) -> float:
    return divident / divisor


print(division(2, 1))
print(division(2, 0))
