from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def wellcome(request):
    name="moslem"
    context={"name":name}

    return render(request,"game/welcome_page.html",context)

def game(request):
    username='moslem1729'
    context={'username':username}

    return render(request,'game/user_page.html',context)