from django.shortcuts import render
from django.http import HttpResponse

def TellHello(requests):
    html = "<h1> 식사하러 갑시다. </h1>"
    return HttpResponse(html)