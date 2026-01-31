from src.temporal.time_decay import decay
from datetime import datetime

def test_decay():
    score = decay(datetime.now())
    assert score > 0
