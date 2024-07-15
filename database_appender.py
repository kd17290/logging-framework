import psycopg2

from log_appender import LogAppender
from log_message import LogMessage


class DatabaseAppender(LogAppender):
    def __init__(self, db_url: str, username: str, password: str):
        self.db_url = db_url
        self.username = username
        self.password = password

    def append(self, log_message: LogMessage):
        try:
            connection = psycopg2.connect(self.db_url, self.username, self.password)
            cursor = connection.cursor()
            level = log_message.get_level().name
            message = log_message.get_message()
            timestamp = log_message.get_timestamp()
            cursor.execute(
                f"INSERT INTO logs ({level}, {message}, {timestamp}) VALUES (%s, %s, %s)"
            )
            connection.commit()
            cursor.close()
            connection.close()
        except psycopg2.Error as e:
            print(f"Error: {e}")
