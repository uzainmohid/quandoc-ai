semantic_cache = {}


def get_cached_response(question):

    return semantic_cache.get(question)


def cache_response(question, response):

    semantic_cache[question] = response