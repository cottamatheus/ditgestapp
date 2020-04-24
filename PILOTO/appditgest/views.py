from django.shortcuts import render, HttpResponse

# Create your views here.

def homeditgest(request):
    descricao = "DITGEST INFO"
    return render(request,"appditgest/home.html", {"desc":descricao})
def login(request):
    return render(request,"appditgest/login.html")
def openaccount(request):
    return HttpResponse("open you account")
