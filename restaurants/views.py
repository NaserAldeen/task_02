from django.shortcuts import render

# Create your views here.

def page_restaurant(request):
    context= {
    "msg": "Hello World!"
    }
    return render(request, 'page.html', context)
