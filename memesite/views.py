# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_user_agents.utils import get_user_agent
from django.views.decorators.csrf import ensure_csrf_cookie
from models import Image, Engagement, Chat, Username
import random, time

def home(request):
	user_agent = get_user_agent(request)
	if user_agent.is_mobile:
		return render(request, "fb_mobile.html")
	elif user_agent.is_tablet:
		return render(request, "fb_mobile.html")
	else:
		return render(request, "fb_home.html")

def newsfeed(request):
	user_agent = get_user_agent(request)
	name = str(request.GET.get("name", None))
	images = Image.objects.all()
	idxs = range(len(images))
	random.shuffle(idxs)
	image = []
	for idx in idxs:
		image.append(images[idx])
	if user_agent.is_mobile:
		return render(request, "newsfeed_mobile.html", {"name": name, 'images': image})
	elif user_agent.is_tablet:
		return render(request, "newsfeed_mobile.html", {"name": name, 'images': image})
	else:
		return render(request, "newsfeed.html", {"name": name, 'images': image})

def engage(request):
	url = str(request.GET.get("url", ""))
	image = [i for i in Image.objects.all() if i.url == url][0]
	image.clicks += 1
	image.save()
	return JsonResponse({'engaged': 'yes', 'clicks': str(image.clicks)})

def update_time(request):
	showtime = 1584405706
	if time.time() > showtime:
		show = "yes"
	else:
		show = "no"
	return JsonResponse({"show": show})

def enter_chat(request):
	name = str(request.GET.get("name", None))
	return render(request, "chat.html", {'username':name})

def add_chat(request):
	text = str(request.GET.get("text", ""))
	name = str(request.GET.get("name", ""))
	if text == "" or name == "":
		return JsonResponse({'status': 'ERROR'})
	chat = Chat()
	chat.name = name
	chat.chat = text
	chat.save()
	return JsonResponse({'status': 'OK'})

def update_chat(request):
	all_chats = Chat.objects.all()
	texts = [str(i.chat) for i in all_chats]
	names = [i.name for i in all_chats]
	return JsonResponse({'texts':texts, 'names':names})

def dev(request):
	user_agent = get_user_agent(request)
	name = str(request.GET.get("name", None))
	images = Image.objects.all()
	idxs = range(len(images))
	random.shuffle(idxs)
	image = []
	for idx in idxs:
		image.append(images[idx])
	if user_agent.is_mobile:
		return render(request, "devfeed.html", {"name": name, 'images': image})
	elif user_agent.is_tablet:
		return render(request, "devfeed.html", {"name": name, 'images': image})
	else:
		return render(request, "devfeed_desktop.html", {"name": name, 'images': image})

def finale(request):
	name = str(request.GET.get("name", None))
	return render(request, "finale.html", {'name': name})
