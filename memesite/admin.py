# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Image, Engagement, Username, Chat

admin.site.register(Image)
admin.site.register(Engagement)
admin.site.register(Username)
admin.site.register(Chat)
