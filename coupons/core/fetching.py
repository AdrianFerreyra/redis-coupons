import logging
import string
import random

import redis

logger = logging.getLogger(__name__)

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


def get_coupon(user_id):
    logger.info(f"getting coupon for user {user_id}")
    assigned_code = r.hget(user_id, "code")
    if assigned_code:
        logger.info(f"coupon {assign_code} found")
        return assigned_code

    logger.info("coupon not found")
    new_assigned_code = assign_code(user_id)
    return new_assigned_code


def assign_code(user_id):
    logger.info(f"assigning coupon to user {user_id}")
    pipeline = r.pipeline()

    pipeline.multi()

    new_code = r.spop("available_codes")
    r.hset(user_id, "code", new_code)

    pipeline.execute()

    return new_code


def setup():
    for code in (
        "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
        for _ in range(10000)
    ):
        logger.info(f"setting code {code}...")
        r.sadd("available_codes", code)


if __name__ == "__main__":
    setup()
