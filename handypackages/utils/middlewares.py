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


def detect_timezone(request, ip):
    timezone_name = "UTC"
    result = requests.get("http://ip-api.com/json/" + ip)
    if result.status_code == 200:
        timezone_name = result.json()['timezone']
        timezone.activate(pytz.timezone(timezone_name))
    return ip + ":" + timezone_name


class IP2TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_and_time_zone = value = request.COOKIES.get('timezone', None)
        ip = get_client_ip(request)
        if not ip_and_time_zone:
            cookie_value = detect_timezone(request, ip)
            response = self.get_response(request)
            response.set_cookie('timezone', cookie_value)
            return response
        else:
            cookie_value = request.COOKIES.get('timezone').split(":")
            if len(cookie_value) != 2:
                return self.get_response(request)
            if ip == cookie_value[0]:
                timezone.activate(pytz.timezone(cookie_value[1]))
                return self.get_response(request)
            else:
                cookie_value = detect_timezone(request, ip)
                response = self.get_response(request)
                response.set_cookie('timezone', cookie_value)
                return response
