from src.orchestration.controller import Controller

def evolve(confidence):
    ctrl = Controller(embedder, store)
    return ctrl.maybe_evolve(confidence, "data/raw")
