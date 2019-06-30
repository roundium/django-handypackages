from handypackages.settings import PASS_DATA_CONTEXT_PROCESSOR


def pass_data(request):
    """
    This context processor will pass data to template
    that you defined in settings.py
    enable context processor:
        'context_processors': [
            ...
            "handypackages.utils.context_processors.pass_data",
            ...
        ]
    example data to pass in settings.py

        PASS_DATA_CONTEXT_PROCESSOR = {
            'base_url': 'https',
            'default_language': LANGUAGE_CODE,
            ...
        }

    templates:
        {{ default_language }}
        {{ base_url }}
        ...
    """
    return PASS_DATA_CONTEXT_PROCESSOR
