"""
for using those context processors you must add the TextPhrase Model
in HANDYTOOLS_MODELS tuple in you settings.py
"""
from handypackages.settings import (TEXT_PHRASE_LANG_CONTEXT_OBJECT_NAME,
                                    TEXT_PHRASE_SIMPLE_CONTEXT_OBJECT_NAME,)
from handypackages.textphrase.models import TextPhrase


def text_phrase_simple_cp(request):
    """
    this context processor will return all text phrases
    enable context processor:
        'context_processors': [
            ...
            "handypackages.textphrase.context_processors.text_phrase_cps.text_phrase_simple_cp",
            ...
        ]
    """
    text_phrases = TextPhrase.objects.all()
    return {
        TEXT_PHRASE_SIMPLE_CONTEXT_OBJECT_NAME: text_phrases
    }


def text_phrase_language_cp(request):
    """
    this context processor will filter text phrase base on current language
    if localization is enabled in yor project and you have
    text phrases for different locales
    it's good idea to use this context processor
    enable context processor:
        'context_processors': [
            ...
            'handypackages.textphrase.context_processors.text_phrase_cps.text_phrase_language_cp',
            ...
        ]
    """
    text_phrases = TextPhrase.objects.filter(language=request.LANGUAGE_CODE)
    return {
        TEXT_PHRASE_LANG_CONTEXT_OBJECT_NAME: text_phrases
    }
