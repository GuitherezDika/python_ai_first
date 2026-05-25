# Configuration
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = BASE_DIR / 'three_basic' / 'data' / 'outputs'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)