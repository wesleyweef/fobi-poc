from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests
from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Dados


@method_decorator(csrf_exempt, name='dispatch')
class CareerPageView(View):
    template_name = "core/career.html"

    def get(self, request):

        return render(request, self.template_name, {'form': ''})

    def post(self, request):

        return render(request, self.template_name, {'form': ''})
        # return redirect('/career/')


@method_decorator(csrf_exempt, name='dispatch')
class JobzoneView(APIView):

    def post(self, request, format=None):

        payload = {'answers': request.data['answers']}

        url = "https://services.onetcenter.org/ws/mnm/interestprofiler/results"

        headers = {
            'Authorization': 'Basic d2VtYXA6NjYyM2p4cA==',
            'Accept': 'application/json'
        }

        response = requests.get(url, headers=headers, params=payload)

        response_json = response.json()

        dados, created = Dados.objects.get_or_create(
            email=request.data['email'],
            defaults={},
        )

        dados.answers = request.data['answers']
        dados.job_zone = response_json

        dados.save()

        return Response(response_json)


@method_decorator(csrf_exempt, name='dispatch')
class CareerView(APIView):

    def post(self, request, format=None):
        payload = {
            'answers': request.data['answers'],
            'job_zone': request.data['job_zone'],
        }

        url = "https://services.onetcenter.org/ws/mnm/interestprofiler/careers"

        headers = {
            'Authorization': 'Basic d2VtYXA6NjYyM2p4cA==',
            'Accept': 'application/json'
        }

        response = requests.get(url, headers=headers, params=payload)

        response_json = response.json()

        dados, created = Dados.objects.get_or_create(
            email=request.data['email'],
            defaults={},
        )

        dados.carrer = response_json

        dados.save()

        return Response(response_json)


def index(request):
    return HttpResponse('<h1>fobi<h1/>')
