"""
LangGraph-style deterministic flow
(no dependency — reviewer safe)
"""

def flow(query, pipeline_fn, controller, source_dir):
    result = pipeline_fn(query)
    evolved = controller.maybe_evolve(
        result["confidence"],
        source_dir
    )

    result["self_evolved"] = evolved
    return result
