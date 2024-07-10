import os
from pathlib import Path

CURRENT_DIR  = Path(__file__).resolve().parent

with open(os.path.join(CURRENT_DIR, "VERSION"), 'rb') as version:
    __version__ = version.read().strip()
    
