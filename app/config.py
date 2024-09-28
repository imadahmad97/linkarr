from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    source_dir = os.getenv("source_dir")
    target_dir = os.getenv("target_dir")
