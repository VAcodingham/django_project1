from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request,someint):
    return HttpResponse(f"placeholder to display blog number: {someint}")
def edit(request,someint):
    return HttpResponse(f"placeholder to edit blog {someint}")
def destroy(request, someint):
    return redirect("/")