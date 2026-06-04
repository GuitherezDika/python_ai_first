from fastapi import Request, HTTPException, Depends
from app.cache.redis_cache import r

MAX_REQUESTS = 10
WINDOW_SECONDS = 60

async def rate_limit(request: Request):
    # ambil IP client
    client_ip = request.client.host
    key = f"rate:{client_ip}"

    count = r.incr(key)

    if count == 1:
        r.expire(key, WINDOW_SECONDS)

    if count > MAX_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail=f"Too many requests. Max {MAX_REQUESTS} per {WINDOW_SECONDS} detik."
        )

