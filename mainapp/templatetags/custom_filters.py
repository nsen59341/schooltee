from django import template
import urllib.parse
import html

register = template.Library()

@register.filter()
def url_decode(value):
    """Decodes a URL-encoded string."""
    return urllib.parse.unquote(html.unescape(value))
