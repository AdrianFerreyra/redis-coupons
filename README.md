# redis-coupons

A simple REST API written in Python using Django that assigns a coupon code per session. Coupons are handled by Redis.

## Architecture

- A Django app that serves HTML on GET `/coupons`. Served through Gunicorn.
- A Redis instance serving as a highly-consistent key-value storage.

## How to use

- Start Docker
- Start Redis `docker-compose up`
- Insert coupons `python -m coupons.core.fetching`
- Start App `make start-app`
