from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello'),

def eggs(request):
    return HttpResponse("YOU GOT EGGS!")
