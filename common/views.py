from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render


class TestView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("더미 URI 입니다.", content_type="application/json")
    
    def post(selfrequest, *args, **kwargs):
        return HttpResponse("더미 URI 입니다.", content_type="application/json")