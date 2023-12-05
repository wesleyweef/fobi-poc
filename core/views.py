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


@method_decorator(csrf_exempt, name='dispatch')
class CareerPageView(View):
    template_name = "core/career.html"

    def get(self, request):
        print('get')
        print(request.GET)
        return render(request, self.template_name, {'form': ''})

    def post(self, request):
        print('post')
        print(request.POST)

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

        return Response(response.json())


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

        return Response(response.json())


def index(request):
    return HttpResponse('<h1>fobi<h1/>')
