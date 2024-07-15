from log_appender import LogAppender


class ConsoleAppender(LogAppender):
    def append(self, log_message: LogAppender):
        print(log_message)
