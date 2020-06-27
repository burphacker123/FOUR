from django.contrib import admin
from .models import NormalProd, PromoProd, about, service 
# Register your models here.
admin.site.register(NormalProd)
admin.site.register(PromoProd)
admin.site.register(about)
admin.site.register(service)