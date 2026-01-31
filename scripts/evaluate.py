from src.evaluation.hallucination_detector import detect_hallucination

def evaluate(answer, context):
    return {
        "hallucination": detect_hallucination(answer, context)
    }
