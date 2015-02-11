#! coding: utf-8
from django import template
from carrousel.models import Carrousel

register = template.Library()


@register.inclusion_tag('carrousel/carrousel.html')
def carousel(slug):
    try:
        current_carousel = Carrousel.objects.get(slug=slug)
        return {
            'carousel': current_carousel,
        }
    except Carrousel.DoesNotExist:
        pass
