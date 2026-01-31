import math
from datetime import datetime

def decay(timestamp, lambda_=0.0005):
    age = (datetime.now() - timestamp).days
    return math.exp(-lambda_ * age)
