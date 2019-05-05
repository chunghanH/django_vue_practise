from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

import json

class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})