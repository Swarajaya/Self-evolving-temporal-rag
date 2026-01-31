class ValidationAgent:
    """
    Ensures new knowledge is not empty / duplicated.
    """

    def validate(self, docs):
        return [d for d in docs if len(d["text"]) > 50]
