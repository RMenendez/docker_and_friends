# src/page_tracker/app.py
"""Module for page_tracker app"""
import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    """AppMain for page_tracker app"""
    try:
        page_views = redis().incr("page_views")
        return f"This page has been seen {page_views} times."

    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{pensive face}", 500


@cache
def redis():
    """Function to connect to redis"""
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
