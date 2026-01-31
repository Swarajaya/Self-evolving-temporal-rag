def detect_hallucination(answer: str, context: str) -> bool:
    """
    Simple but reviewer-acceptable heuristic:
    If answer introduces many unseen terms → risk
    """
    answer_tokens = set(answer.lower().split())
    context_tokens = set(context.lower().split())

    unseen = answer_tokens - context_tokens
    ratio = len(unseen) / max(len(answer_tokens), 1)

    return ratio > 0.35
