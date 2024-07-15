from console_appender import ConsoleAppender
from log_config import LogConfig
from log_level import LogLevel
from logger import Logger


def run():
    logger: Logger = Logger.get_instance()
    appender = ConsoleAppender()
    log_config = LogConfig(appender, LogLevel.DEBUG)
    logger.set_config(log_config)
    logger.debug("This is debug message")
    logger.info("This is info message")
    logger.warning("This is warning message")
    logger.error("This is error message")
    logger.critical("This is critical message")


if __name__ == "__main__":
    run()
