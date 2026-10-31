"""Read application configuration from environment variables."""
import os
from dataclasses import dataclass

from dotenv import load_dotenv


# Load local development settings if a .env file exists.
# Existing environment variables take precedence by default.
load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_env: str
    data_file: str


def load_settings() -> Settings:
    """Load non-secret application settings with safe defaults."""
    return Settings(
        app_env=os.getenv("APP_ENV", "development"),
        data_file=os.getenv("TASKS_FILE", "data/tasks.json"),
    )
