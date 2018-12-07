# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .addons import app_conj
import random

# Create your views here.
def index(request):
	if not 'verb' in request.GET:
		verb = [i for i in app_conj.data_verbe_translate]
		verb = random.choice(verb)
	else:
		verb = request.GET['verb']
	data =[i.split(' || ') for i in app_conj.conjuguer(verb)]
	title = data[0][0]
	data = data[1:]
	_ = [i*7 for i in range(len(data))][:int(len(data)/6)]
	conjs = {}
	for i in range(len(data)):
		if i in _:
			tag = data[i]
			conjs[tag[0]] = []
		else:
			conjs[tag[0]].append(data[i])
	#return HttpResponse(str(conjs))
	url = request.path+'?verb=%s'%verb
	return render(request, 'conj/index.html', locals())