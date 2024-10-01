from django.shortcuts import render
# Additional importings
from django.http import HttpResponse, JsonResponse
import random
import string

# Create your views here.
def home(request):
    return render(request, "home.html")

def passgen(request):
    """length = int(request.GET.get('length', 8))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'index.html', {'password' :password})"""
    
    char = list("abcdefghijklmnopqrstuvwxyz") # The default password chars will be all small letters 
    if request.GET.get("uppercase"):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('digits'):
        char.extend(list('0123456789'))
    if request.GET.get('symbol'):
        char.extend("\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~!")

    length = int(request.GET.get('length', 10))
    password = ""
    for x in range(length):
        password += random.choice(char)
    return render(request, "password.html", {'password':password})
