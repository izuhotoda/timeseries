from django.shortcuts import render
from django.views.generic import ListView
from .models import Temperature

# Create your views here.
class IndexView(ListView):
	template_name = 'logger/index.html'
	def get_queryset(self):
		return Temperature.objects.all()