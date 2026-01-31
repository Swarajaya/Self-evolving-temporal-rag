from .time_decay import decay

def rerank(results):
    ranked = []
    for meta, dist in results:
        sim = 1 / (1 + dist)
        score = sim * decay(meta["timestamp"])
        ranked.append((meta, score))
    return sorted(ranked, key=lambda x: x[1], reverse=True)
