import requests
import pytz
from django.utils import timezone


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class IP2TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = get_client_ip(request)
        result = requests.get("http://ip-api.com/json/" + ip)
        if result.status_code == 200:
            timezone_name = result.json()['timezone']
            timezone.activate(pytz.timezone(timezone_name))
        response = self.get_response(request)
        return response
