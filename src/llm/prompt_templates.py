def qa_prompt(context, query):
    return f"""
Use ONLY the context below.

Context:
{context}

Question:
{query}
"""
