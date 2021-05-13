import redis

from vars import var

INFO = var.REDIS_URI.split(":")

DB = redis.StrictRedis(
    host=INFO[0],
    port=INFO[1],
    password=var.REDIS_PASS,
    charset="utf-8",
    decode_responses=True,
)
