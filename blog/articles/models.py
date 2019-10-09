# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    # thumbnail
    # author
    # tags

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'