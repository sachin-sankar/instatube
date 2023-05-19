from loguru import logger as log
log.add("log.txt", rotation="1 week",backtrace=True)