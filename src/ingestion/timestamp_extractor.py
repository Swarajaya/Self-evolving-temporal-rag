import re
from datetime import datetime

def extract_timestamp(text: str):
    match = re.search(r"(19|20)\d{2}", text)
    if match:
        return datetime(int(match.group()), 1, 1)
    return datetime.now()
