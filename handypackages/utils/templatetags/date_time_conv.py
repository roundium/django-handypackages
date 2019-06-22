from datetime import datetime

from django import template

from handypackages.datetime_conv import fmt

register = template.Library()


@register.filter(name="persian_datetime")
def datetime_conv(date_time, string_format="%y/%m/%d %h:%M:%s"):
    """
    Convert datetime to persian datetime
    example(datetime=datetime.datetime(2019, 5, 28, 1, 10, 33)):
        {% load date_time_conv %}
        {{ datetime|datetime_conv:"%y/%m/%d %h:%M:%s" }}
    output => 1398/3/7 1:10:33
    """
    if not isinstance(date_time, datetime):
        raise template.TemplateSyntaxError(
            "datetime_conv first argument must be datetime instance.",
        )
    return fmt(date_time, string_format)
