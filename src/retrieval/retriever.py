from ..temporal.temporal_ranker import rerank

def retrieve(store, query_vec, k=5):
    results = store.search(query_vec, k)
    return rerank(results)
