# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Image(models.Model):
	url = models.CharField(max_length=500)
	clicks = models.IntegerField(default=0)

	def __str__(self):
		return self.url

class Engagement(models.Model):
	name = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Chat(models.Model):
	name = models.CharField(max_length=500)
	chat = models.TextField()

	def __str__(self):
		return self.chat

class Username(models.Model):
	name = models.CharField(max_length=500)

	def __str__(self):
		return self.name
