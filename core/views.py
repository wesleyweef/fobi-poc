from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests


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
