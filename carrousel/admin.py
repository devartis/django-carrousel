#! coding: utf-8
from django.contrib import admin
from carrousel.models import Slide, Carrousel

admin.site.register(Carrousel)
admin.site.register(Slide)

__author__ = 'poli'
