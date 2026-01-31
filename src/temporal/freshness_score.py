from datetime import datetime

def freshness(timestamp):
    return 1 / (1 + (datetime.now() - timestamp).days)
