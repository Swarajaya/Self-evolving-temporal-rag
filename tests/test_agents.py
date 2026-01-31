from src.agents.self_evolve_agent import SelfEvolveAgent

def test_evolution_trigger():
    agent = SelfEvolveAgent()
    assert agent.should_evolve(0.2) is True
