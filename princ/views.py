from django.shortcuts import render
from .models import NormalProd, PromoProd, about, service
# Create your views here.
def index(request):
    prodn = NormalProd.objects.all()
    prodp = PromoProd.objects.all()
    abt = about.objects.all()
    services = service.objects.all()
    return render(request, 'index.html', {'normal': prodn, 'promo': prodp, 'about': abt,'ser':services })
