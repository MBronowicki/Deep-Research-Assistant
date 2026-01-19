# config.py
from json import load
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def get_env_variable(env_var_name: str, required: bool = True, default = None) -> str:
    "Load an environment variable safely."
    value = os.getenv(env_var_name, default)
    if required and value is None:
        raise ValueError(f"{env_var_name} variable not set in .env")
    return value