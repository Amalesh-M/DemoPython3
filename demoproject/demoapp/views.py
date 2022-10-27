from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import team
# Create your views here.
def demo(request):
   obj=Place.objects.all()
   object=team.objects.all()
   name="india"
   return render(request, "static.html", {'result': obj, 'result2': object})


