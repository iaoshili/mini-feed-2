import json
from functools import wraps

import redis


def redis_connect() -> redis.client.Redis:
    return redis.Redis(host='redis', port=6379, db=0, password="eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81")

global_cache = redis_connect()


# From https://gist.github.com/mminer/34d4746fa82b75182ee7
def cached(func):
    """
    Decorator that caches the results of the function call.

    We use Redis in this example, but any cache (e.g. memcached) will work.
    We also assume that the result of the function can be seralized as JSON,
    which obviously will be untrue in many situations. Tweak as needed.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Generate the cache key from the function's arguments.
        key_parts = [func.__name__] + list(args)
        key = '-'.join(key_parts)
        result = global_cache.get(key)

        if result is None:
            # Run the function and cache the result for next time.
            value = func(*args, **kwargs)
            value_json = json.dumps(value)
            global_cache.set(key, value_json)
        else:
            # Skip the function entirely and use the cached value instead.
            value_json = result.decode('utf-8')
            value = json.loads(value_json)

        return value
    return wrapper
