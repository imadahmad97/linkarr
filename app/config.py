from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    target_dir = os.getenv("target_dir")


print(f"Loaded target_dir: {Config.target_dir}")
