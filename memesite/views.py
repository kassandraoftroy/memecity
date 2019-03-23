# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_user_agents.utils import get_user_agent
from django.views.decorators.csrf import ensure_csrf_cookie
from models import Image, Engagement
import random, time

def home(request):
	user_agent = get_user_agent(request)
	if user_agent.is_mobile:
		return render(request, "encrypted_mobile.html")
	elif user_agent.is_tablet:
		return render(request, "encrypted_mobile.html")
	else:
		return render(request, "encrypted_pc.html")

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

def update_time(request):
	now = time.time() #current epoch time
	dist = 1553616000 - now #returns seconds
	days = int(dist // 86400)
	hours = int(dist // 3600 % 24)
	minutes = int(dist // 60 % 60)
	seconds = int(dist % 60)
	return JsonResponse({'days':str(days), 'hours': str(hours), 'minutes': str(minutes), 'seconds': str(seconds)})


