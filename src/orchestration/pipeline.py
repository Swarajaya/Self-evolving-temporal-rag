from ..evaluation.confidence_scorer import confidence

def run(query, embedder, store, retriever, llm):
    qvec = embedder.encode([query])[0]
    ranked = retriever(store, qvec)
    scores = [s for _, s in ranked]

    context = "\n".join([d["text"] for d, _ in ranked[:3]])
    answer = llm.generate(context)

    return {
        "answer": answer,
        "confidence": confidence(scores)
    }
