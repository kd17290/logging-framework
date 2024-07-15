from log_appender import LogAppender
from log_level import LogLevel


class LogConfig:
    log_appender: LogAppender
    log_level: LogLevel

    def __init__(self, log_appender: LogAppender, log_level: LogLevel):
        self.log_appender = log_appender
        self.log_level = log_level

    def get_log_level(self):
        return self.log_level

    def get_log_appender(self):
        return self.log_appender

    def set_log_level(self, log_level: LogLevel):
        self.log_level = log_level

    def set_log_appender(self, log_appender: LogAppender):
        self.log_appender = log_appender
