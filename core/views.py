from django.shortcuts import render,redirect
from accounts.forms import *
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import json
import http.client

def home(request):
	template_name = 'index.html'
	return render(request, template_name)

class Rest(APIView):
	permission_classes = (IsAuthenticatedOrReadOnly,)
	def get(self,request,format=None):

		connection = http.client.HTTPSConnection('api.parse.com', 443)
		connection.connect()
		connection.request('POST', '/1/classes/GameScore', json.dumps({
			   "score": 1337,
			   "playerName": "Sean Plott",
			   "cheatMode": False
			 }), {
			   "X-Parse-Application-Id": "fww6sQUA36kG6OjOPzRB2ELCJpJiFJtmS0lnx1fB",
			   "X-Parse-REST-API-Key": "wf7H3KAHYKcd5oeyQgc20BEIOtktEvlqug3E2ND7",
			   "Content-Type": "application/json"
			 })
		print('KKKKKKKKKKKKKK')
		results = json.loads(connection.getresponse().read())
		print('KKKKKKKKKKKKKK')
		print(results)
		return Response({'mensagem': 'Olá'})

rest = Rest.as_view()

# class Rest(APIView):
# 	permission_classes = (IsAuthenticatedOrReadOnly)
# 	# parser_classes = (JSONParser,)
# 	# @api_view(['POST'])
# 	# @parser_classes((JSONParser,))
# 	def get(self,request,format=None):
# 		return Response({'mensagem': 'Olá'})
#
# rest = Rest.as_view()

def register(request):

	template_name = 'doctor/register.html'
	form = RegisterForm_Doctor(request.POST)
	contexto = {}
	if request.method == "POST":
		if form.is_valid():
			user = form.save()
			messages.success(request, 'Seu cadastro foi feito com sucesso!')
			user = authenticate(username = user.username, password = form.cleaned_data['password1'])
			user.save()
			return redirect('accounts:dashboard')
	else:
		form = RegisterForm_Doctor()
	contexto['form'] = form
	return render(request, template_name, contexto)
