#! coding: utf-8
from django import template
from slider.models import Carousel

register = template.Library()


@register.inclusion_tag('slider/slider.html')
def carousel(slug):
    try:
        current_carousel = Carousel.objects.get(slug=slug)
        return {
            'carousel': current_carousel,
        }
    except Carousel.DoesNotExist:
        pass
