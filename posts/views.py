from django.shortcuts import render
from django.http import HttpResponse

def answer_view(request):
    return HttpResponse("<h1>My answer:</h1>")
# Create your views here.
def second_view(request):
    return render(request, 'base.html')
