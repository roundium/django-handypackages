import datetime

from django.test import TestCase

from .datetime_conv import (gregorian_to_jd, jd_to_gregorian, jd_to_persian,
                            persian_to_jd, fmt)


class TestDateTimeConv(TestCase):
    def test_gregorian_to_persian(self):
        jd = gregorian_to_jd(2019, 5, 28)
        persian_date = jd_to_persian(jd)
        persian_date = "/".join(persian_date)
        self.assertEqual(persian_date, "1398/3/7")

    def test_persian_to_gregorian(self):
        jd = persian_to_jd(1398, 3, 7)
        gregorian = jd_to_gregorian(jd)
        gregorian_date = "/".join(gregorian)
        self.assertEqual(gregorian_date, "2019/5/28")

    def test_persian_date_formatter(self):
        date = datetime.datetime(2019, 5, 28, 1, 10, 33)
        persian_date = fmt(date)
        self.assertEqual(persian_date, "1398/3/7 1:10:33")

        persian_date = fmt(date, "%h:%M:%s %d/%m/%y")
        self.assertEqual(persian_date, "1:10:33 7/3/1398")

        persian_date = fmt(date, "%y %n %d")
        self.assertEqual(persian_date, "1398 خرداد 7")
