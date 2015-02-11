#! coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from positions import PositionField
from easy_thumbnails.fields import ThumbnailerImageField

SLIDE_HTML_POSITION_CHOICES = (
    ('left-top', _('Top-Left'), ),
    ('left-mid', _('Middle-Left'), ),
    ('left-bot', _('Bottom-Left'), ),
    ('center-top', _('Top-Center'), ),
    ('center-mid', _('Middle-Center'), ),
    ('center-bot', _('Bottom-Center'), ),
    ('right-top', _('Top-Right'), ),
    ('right-mid', _('Middle-Right'), ),
    ('right-bot', _('Bottom-right'), ),
)


class Carrousel(models.Model):
    class Meta:
        verbose_name = _('carrousel')

    name = models.CharField(max_length=100, verbose_name=_('name'))
    slug = models.CharField(max_length=100, unique=True, verbose_name=_('slug'))
    interval = models.IntegerField(verbose_name=_('interval'))
    show_indicators = models.BooleanField(verbose_name=_('show indicators'), default=False)

    def __unicode__(self):
        return self.name


class Slide(models.Model):
    class Meta:
        verbose_name = _('slide')
        ordering = ['position', ]

    carrousel = models.ForeignKey(Carrousel, related_name='slides', verbose_name=_('carrousel'))

    name = models.CharField(max_length=100, verbose_name=_('name'))
    position = PositionField(verbose_name=_('position'))
    image = ThumbnailerImageField(upload_to='slider/', blank=True, null=True, verbose_name=_('image'))
    mobile_image = ThumbnailerImageField(upload_to='slider/', blank=True, null=True, verbose_name=_('mobile image'))
    html = models.TextField(blank=True, null=True, verbose_name=_('html'))
    html_position = models.CharField(max_length=30, blank=True, null=True, verbose_name=_('html position'),
                                     choices=SLIDE_HTML_POSITION_CHOICES)
    url = models.URLField(blank=True, null=True, verbose_name=_('url'))

    def __unicode__(self):
        return self.name
