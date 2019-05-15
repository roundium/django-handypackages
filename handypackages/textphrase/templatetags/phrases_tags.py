from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def single_text_phrase(context, phrase_type=None, language=None):
    """
    for using this template tag you must
    enable one of the text_phrase context_processors.
    this templatetag will return the first text phrase object,
    if there is more then one object.
    if you want single text phrase in special language set the language arg.
    example:
            {% load phrases_tags %}
            {% single_text_phrase "language" "en" as lang %}
            <p>{{ lang.text }}</p>
    """
    phrases = context.get('text_phrases', None)
    if not phrases:
        raise Exception(
            "for using single_text_phrase templatetag, "
            "Please Enable one of the Text Phrase Context Processors"
        )
    if not language:
        phrase = phrases.filter(phrase_type=phrase_type)
        return phrase.first()
    phrase = phrases.filter(phrase_type=phrase_type, language=language)
    return phrase.first()


@register.simple_tag(takes_context=True)
def multi_text_phrase(context, phrase_type=None, language=None):
    """
    for using this template tag you must
    enable one of text_phrase context_processors.
    this templatetag will return list of text phrases
    that have this phrase_type.
    if you want single text phrase in special language set the language arg.
    example:
            {% load phrases_tags %}
            {% multi_text_phrase "language" as languages %}
            {% for lang in languages %}
                <p>{{ lang.text }}</p>
            {% endfor %}
    """
    phrases = context.get('text_phrases', None)
    if not phrases:
        raise Exception(
            "for using single_text_phrase templatetag, "
            "Please Enable one of the Text Phrase Context Processors"
        )
    if not language:
        return phrases.filter(phrase_type=phrase_type)
    return phrases.filter(phrase_type=phrase_type, language=language)
