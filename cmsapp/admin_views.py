from django.http import HttpResponseRedirect
from django.shortcuts import render
from cmsapp.models import Client
from django.contrib import messages
from django.urls import reverse

def render_dashboard(request):
    return render(request, "admin_templates/dashboard.html")

def render_clients(request):
    clients = Client.objects.all()
    data = {
        "clients": clients
    }
    print(data)
    return render(request, "admin_templates/clients.html", context=data)

def add_clients(request):
    companyname = request.POST.get("companyname")
    contactperson = request.POST.get("contactperson")
    phonenumber = request.POST.get("phonenumber")
    email = request.POST.get("email")
    countryname = request.POST.get("countryname")
    cityname = request.POST.get("cityname")
    address = request.POST.get("address")
    client_obj = Client(companyname=companyname, contactperson=contactperson, phonenumber=phonenumber, email=email, countryname=countryname, cityname=cityname, address=address)
    client_obj.save()
    messages.success(request, "Client Added Successfully!")
    return HttpResponseRedirect(reverse("clients"))

def render_projects(request):
    return render(request, "admin_templates/projects.html")