import redis
import hashlib

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

CACHE_TTL = 60 * 60 # 1 jam

def make_key(message: str) -> str:
    # hash pesan jadi key yang pendek dan konsisten
    # ubah pesan jadi key pendek
    return "chat:" + hashlib.md5(message.encode()).hexdigest()

def get_cache(message: str) -> str | None:
    key = make_key(message)
    return r.get(key)

def set_cache(message: str, response: str):
    key = make_key(message)
    # simpan cache dan akan otomatis hilang setelah 1 jam
    r.setex(key, CACHE_TTL, response)