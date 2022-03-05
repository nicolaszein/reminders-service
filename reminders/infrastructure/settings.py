import os
from typing import Optional

from yarl import URL


class Settings:
    @property
    def region(self):
        return self.__get("AWS_DEFAULT_REGION")

    @property
    def dynamodb_url(self):
        dynamodb_url = self.__get("DYNAMODB_URL")
        return URL(dynamodb_url) if dynamodb_url else None

    @property
    def log_level(self):
        return self.__get("LOG_LEVEL", "INFO").upper()

    @property
    def service_data_table_name(self):
        return self.__get("DATA_TABLE", "reminders-dev-data")

    @staticmethod
    def __get(key, default_value=None):
        return os.getenv(key, default_value)
