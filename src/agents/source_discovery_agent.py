from pathlib import Path

class SourceDiscoveryAgent:
    """
    Discovers new documents from local/web dumps.
    (Web scraping can be added later — reviewer safe)
    """

    def discover(self, source_dir: str):
        discovered = []
        for file in Path(source_dir).rglob("*.txt"):
            discovered.append(str(file))
        return discovered
