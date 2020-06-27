from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart
from princ.models import NormalProd
# Create your views here.
def cart(request):
    cart = Cart.objects.all()[0]
    return render(request, 'cart/view.html', {'cart': cart})
def update(request, slug):
    cart = Cart.objects.all()[0]
    try:
        productes = NormalProd.objects.filter(slug=slug).order_by('id').first()
    except NormalProd.DoesNotExist:
        pass
    if not productes in cart.products.all():
        cart.products.add(productes)
    else:
        cart.products.remove(productes)
    return HttpResponseRedirect(reverse("cart"))
