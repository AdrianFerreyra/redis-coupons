import uuid
from django.http import HttpResponse
from django.shortcuts import render

from coupons.core.fetching import get_coupon


def get_cookie(request):
    return request.COOKIES.get("user_id")


def new_user_id():
    return str(uuid.uuid4())


def index(request):
    user_id = get_cookie(request)
    if not user_id:
        user_id = new_user_id()
    coupon = get_coupon(user_id)
    response = HttpResponse(f"Your coupon is: {coupon}")
    response.set_cookie("user_id", user_id)
    return response
