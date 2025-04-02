
import redis

def redis_operations():
    # Create a Redis client
    redis_client = redis.Redis(host='localhost', port=6379, db=0)

    # Set a key-value pair
    redis_client.set('greeting', 'Hello, Redis!')

    # Get the value for a key
    value = redis_client.get('greeting')
    greeting = value.decode('utf-8') if value else None

    # Increment a counter
    redis_client.incr('visitor_count')

    # Get the current count
    count = redis_client.get('visitor_count')
    visitor_count = count.decode('utf-8') if count else '0'

    # Delete a key
    redis_client.delete('greeting')

    # Check if a key exists
    exists = redis_client.exists('greeting')

    # Return results for Benchify to capture
    return {
        "greeting": greeting,
        "visitor_count": visitor_count,
        "greeting_exists_after_delete": bool(exists)
    }
