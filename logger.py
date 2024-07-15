from console_appender import ConsoleAppender
from log_config import LogConfig
from log_level import LogLevel
from log_message import LogMessage


class Logger:
    _instance = None
    config: LogConfig

    def __init__(self):
        if self._instance is not None:
            raise Exception("This class is a singleton!")
        Logger._instance = self
        self.config = LogConfig(log_appender=ConsoleAppender(), log_level=LogLevel.INFO)

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger()
        return Logger._instance

    def set_config(self, config: LogConfig):
        self.config = config

    def log(self, level: LogLevel, content: str):
        if level.value >= self.config.get_log_level().value:
            log_message = LogMessage(level, content)
            self.config.get_log_appender().append(log_message)

    def debug(self, content: str):
        self.log(LogLevel.DEBUG, content)

    def info(self, content: str):
        self.log(LogLevel.INFO, content)

    def warning(self, content: str):
        self.log(LogLevel.WARNING, content)

    def error(self, content: str):
        self.log(LogLevel.ERROR, content)

    def critical(self, content: str):
        self.log(LogLevel.CRITICAL, content)

    def exception(self, content: str):
        self.log(LogLevel.ERROR, content)
