import cgi
import math
import string


Weekdays = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]


def mod(a, b):
    return a - (b * math.floor(a / b))


def leap_gregorian(year):
    return (
        (year % 4) == 0) and (not (
            ((year % 100) == 0) and ((year % 400) != 0)))


GREGORIAN_EPOCH = 1721425.5


def gregorian_to_jd(year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    return (GREGORIAN_EPOCH - 1) + (365 * (year - 1)) +\
        math.floor((year - 1) / 4) + (-math.floor((year - 1) / 100)) +\
        math.floor((year - 1) / 400) +\
        math.floor((((367 * month) - 362) / 12) +
                   (0 if month <= 2 else -1 if leap_gregorian(year) else -2) +
                   day)


def jd_to_gregorian(jd):
    wjd = math.floor(jd - 0.5) + 0.5

    depoch = wjd - GREGORIAN_EPOCH
    quadricent = math.floor(depoch / 146097)
    dqc = mod(depoch, 146097)
    cent = math.floor(dqc / 36524)
    dcent = mod(dqc, 36524)
    quad = math.floor(dcent / 1461)
    dquad = mod(dcent, 1461)
    yindex = math.floor(dquad / 365)
    year = (quadricent * 400) + (cent * 100) + (quad * 4) + yindex

    if (not (cent == 4 or yindex == 4)):
        year += 1

    yearday = wjd - gregorian_to_jd(year, 1, 1)

    leapadj = 0 if wjd < gregorian_to_jd(
        year, 3, 1) else 1 if leap_gregorian(year) else 2

    month = math.floor((((yearday + leapadj) * 12) + 373) / 367)
    day = (wjd - gregorian_to_jd(year, month, 1)) + 1

    return map(str, [year, month, int(day)])


PERSIAN_EPOCH = 1948320.5


def persian_to_jd(year, month, day):
    epbase = year - 474 if year >= 0 else 473
    epyear = 474 + (epbase % 2820)

    return day + (((month - 1) * 31) if (month <= 7) else((
        (month - 1) * 30) + 6)
    ) + math.floor(
        ((epyear * 682) - 110) / 2816) + (epyear - 1) * 365 +\
        math.floor(epbase / 2820) * 1029983 + (PERSIAN_EPOCH - 1)


def jd_to_persian(jd):
    jd = math.floor(jd) + 0.5

    depoch = jd - persian_to_jd(475, 1, 1)
    cycle = math.floor(depoch / 1029983)
    cyear = depoch % 1029983
    if cyear == 1029982:
        ycycle = 2820
    else:
        aux1 = math.floor(cyear / 366)
        aux2 = mod(cyear, 366)
        ycycle = math.floor(
            ((2134 * aux1) + (2816 * aux2) + 2815) / 1028522) + aux1 + 1

    year = ycycle + (2820 * cycle) + 474
    if (year <= 0):
        year -= 1

    yday = (jd - persian_to_jd(year, 1, 1)) + 1
    month = math.ceil(yday / 31) if (yday <=
                                     186) else math.ceil((yday - 6) / 30)
    day = (jd - persian_to_jd(year, month, 1)) + 1
    return map(str, [year, month, int(day)])


class _PersianDateTimeFormatter(string.Formatter):
    def format_field(self, value, spec):
        value = cgi.escape(value)
        spec = spec[:-1] + 's'
        return super(_PersianDateTimeFormatter, self).format_field(value, spec)


replaces = {
    "%y": "{year:y}",
    "%m": "{month:m}",
    "%n": "{month_name:n}",
    "%d": "{day:d}",
    "%h": "{hour:h}",
    "%M": "{minute:M}",
    "%s": "{second:s}",
}

persian_month_names = [
    "persian_month_names",
    "فروردین",
    "ادریبهشت",
    "خرداد",
    "تیر",
    "مرداد",
    "شهریور",
    "مهر",
    "ابان",
    "اذر",
    "دی",
    "بهمن",
    "اسفند"
]


def _do_replace(format):
    for k, v in replaces.items():
        format = format.replace(k, v)
    return format


def fmt(date_time, format="%y/%m/%d %h:%M:%s"):
    format = _do_replace(format)
    jd = gregorian_to_jd(date_time.year, date_time.month, date_time.day)
    persian_date = list(jd_to_persian(jd))
    date_dict = {
        "year": persian_date[0],
        "month": persian_date[1],
        "month_name": persian_month_names[int(persian_date[1])],
        "day": persian_date[2],
        "hour": str(date_time.hour),
        "minute": str(date_time.minute),
        "second": str(date_time.second),
    }
    return _PersianDateTimeFormatter().format(format, **date_dict)
