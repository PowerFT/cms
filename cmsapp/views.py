from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def render_home(request):
    return render(request, "website_templates/home.html")
def render_about(request):
    return render(request, "website_templates/about.html")
def render_contact(request):
    return render(request, "website_templates/contact.html")
def render_login(request):
    return render(request, "website_templates/login.html")
def render_signup(request):
    return render(request, "website_templates/signup.html")
def perform_login(request):
    un = request.POST.get("username")
    ps = request.POST.get("password")
    user = authenticate(username=un, password=ps) # None
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        messages.error(request, "Invalid Username or Password")
        return HttpResponseRedirect(reverse("render_login"))
def perform_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))