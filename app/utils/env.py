from typing import Any, Generic, Union
from dotenv import load_dotenv
import os


ENV_FILE_PATH = os.getenv('ENV_FILE_PATH', '../resources/.env')

load_dotenv(ENV_FILE_PATH)


def env(key: str, default=None) -> Union[str, Any]:
    return os.getenv(key, default)
