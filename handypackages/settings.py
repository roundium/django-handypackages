from django.conf import settings

TEXT_PHRASE_MODEL_PHRASE_TYPES = getattr(
    settings, 'TEXT_PHRASE_MODEL_PHRASES_TYPES', [])

TEXT_PHRASE_SIMPLE_CONTEXT_OBJECT_NAME = getattr(
    settings, 'TEXT_PHRASE_SIMPLE_CONTEXT_OBJECT_NAME', 'text_phrases')

TEXT_PHRASE_LANG_CONTEXT_OBJECT_NAME = getattr(
    settings, 'TEXT_PHRASE_LANG_CONTEXT_OBJECT_NAME', 'text_phrases_lang')

PASS_DATA_CONTEXT_PROCESSOR = getattr(
    settings, 'PASS_DATA_CONTEXT_PROCESSOR', {})

ALL_LANGUAGES = getattr(settings, 'LANGUAGES', [])

TIMEZONE_COOKIE_NAME = getattr(settings, 'TIMEZONE_COOKIE_NAME', "timezone")

def _get_languages():
    """
    generate language list with Global Key
    for language independent phrases
    """
    language_list = [
        ('global', 'Global')
    ]
    for item in ALL_LANGUAGES:
        language_list.append(item)
    return language_list


TEXT_PHRASE_LANGUAGES = _get_languages
