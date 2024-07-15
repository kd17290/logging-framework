from log_appender import LogAppender
from log_message import LogMessage


class FileAppender(LogAppender):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def append(self, log_message: LogMessage):
        with open(self.file_path, "a+") as file:
            file.write(str(log_message) + "\n")
