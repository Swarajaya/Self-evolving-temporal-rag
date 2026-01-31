class SelfEvolveAgent:
    def __init__(self, threshold=0.55):
        self.threshold = threshold

    def should_evolve(self, confidence: float) -> bool:
        return confidence < self.threshold
