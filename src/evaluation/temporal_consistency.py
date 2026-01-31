from datetime import datetime

def temporal_consistency(timestamps):
    if not timestamps:
        return 0.0

    now = datetime.now()
    avg_age = sum([(now - t).days for t in timestamps]) / len(timestamps)
    return 1 / (1 + avg_age)
