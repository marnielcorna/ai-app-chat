import os
from dotenv import load_dotenv

load_dotenv()

DB_ENV = os.getenv("DB_ENV", "local")


def get_db_config():
    return {
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "name": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
    }


def build_db_url():
    config = get_db_config()
    return (
        f"postgresql://{config['user']}:{config['password']}@"
        f"{config['host']}:{config['port']}/{config['name']}"
    )
