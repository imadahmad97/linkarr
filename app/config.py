from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    target_dir = os.getenv("target_dir")
