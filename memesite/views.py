# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_user_agents.utils import get_user_agent
from django.views.decorators.csrf import ensure_csrf_cookie
from models import Image, Engagement
import random

def home(request):
	user_agent = get_user_agent(request)
	if user_agent.is_mobile:
		return render(request, "home.html")
	elif user_agent.is_tablet:
		return render(request, "home.html")
	else:
		return render(request, "homepc.html")

def switch_image(request):
	image = random.choice(Image.objects.all())
	engage = random.choice(Engagement.objects.all())
	return JsonResponse({'url': image.url, 'text':engage.name, 'clicks': str(image.clicks), 'engaged': 'no'})

def engage(request):
	url = str(request.GET.get("url", ""))
	image = [i for i in Image.objects.all() if i.url == url][0]
	image.clicks += 1
	image.save()
	return JsonResponse({'engaged': 'yes', 'clicks': str(image.clicks)})


