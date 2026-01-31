from ..agents.self_evolve_agent import SelfEvolveAgent
from ..agents.source_discovery_agent import SourceDiscoveryAgent
from ..agents.update_agent import UpdateAgent

class Controller:
    def __init__(self, embedder, store):
        self.evolver = SelfEvolveAgent()
        self.discoverer = SourceDiscoveryAgent()
        self.updater = UpdateAgent(embedder, store)

    def maybe_evolve(self, confidence, source_dir):
        if not self.evolver.should_evolve(confidence):
            return False

        new_sources = self.discoverer.discover(source_dir)
        added = self.updater.update_from_sources(new_sources)
        return added > 0
