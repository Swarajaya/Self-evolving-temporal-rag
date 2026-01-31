def is_time_sensitive(query: str) -> bool:
    keywords = ["latest", "current", "recent", "new", "today"]
    return any(k in query.lower() for k in keywords)
