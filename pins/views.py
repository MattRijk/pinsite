from django.shortcuts import render, get_object_or_404
from pins.models import Category
# Create your views here.

def home(requests):
    return render(requests, 'HomePage.html', {})


def category(request, slug):
    context = {
        "category": get_object_or_404(Category, slug=slug)
    }
    return render(request, "Category.html", context)