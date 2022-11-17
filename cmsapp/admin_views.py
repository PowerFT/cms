# Importing Dependencies
from django.http import HttpResponseRedirect
from django.shortcuts import render
from cmsapp.models import Client, Project
from django.contrib import messages
from django.urls import reverse

# Dashboard
def render_dashboard(request):
    clients = Client.objects.all()
    projects = Project.objects.all()
    print(projects)
    total = 0
    for project in projects:
        total += project.amount
    print(total)
    data = {
        "no_of_clients": len(clients),
        "no_of_projects": len(projects),
        "total_amount": total,
        "recent_project": projects[len(projects) - 1]
    }
    return render(request, "admin_templates/dashboard.html", data)

# Clients

# Render Clients Page
def render_clients(request):
    clients = Client.objects.all()
    data = {
        "clients": clients
    }
    print(data)
    return render(request, "admin_templates/clients.html", context=data)
# Adding the client to the database
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
# Rendering the Edit Clients Page
def edit_clients(request, mainid):
    client = Client.objects.get(mainid=mainid)
    context = {
        "client": client,
        "clientid": mainid
    }
    return render(request, "admin_templates/edit_clients.html", context=context)
# Rendering the More Information Page
def view_clients(request, mainid):
    client = Client.objects.get(mainid=mainid)
    context = {
        "client": client,
        "clientid": mainid
    }
    return render(request, "admin_templates/view_clients.html", context=context)
# Rendering the Delete Clients Page
def delete_clients(request, mainid):
    client = Client.objects.get(mainid=mainid)
    context = {
        "client": client,
        "clientid": mainid
    }
    return render(request, "admin_templates/delete_clients.html", context=context)
# Performing the operation of editing a client
def edit_client(request):
    mainid = request.POST.get("mainid")
    companyname = request.POST.get("companyname")
    contactperson = request.POST.get("contactperson")
    phonenumber = request.POST.get("phonenumber")
    email = request.POST.get("email")
    countryname = request.POST.get("countryname")
    cityname = request.POST.get("cityname")
    address = request.POST.get("address")
    client_obj = Client.objects.get(mainid=mainid)
    client_obj.companyname = companyname
    client_obj.contactperson = contactperson
    client_obj.phonenumber = phonenumber
    client_obj.email = email
    client_obj.countryname = countryname
    client_obj.cityname = cityname
    client_obj.address = address
    client_obj.save()
    messages.success(request, "Client Updated Successfully!")
    return HttpResponseRedirect(reverse("clients"))
# Performing the operation of deleting a client
def delete_client(request):
    mainid = request.POST.get("mainid")
    client_obj = Client.objects.get(mainid= mainid)
    client_obj.delete()
    messages.success(request, "Client Deleted Successfully!")
    return HttpResponseRedirect(reverse("clients"))




# Projects


# Rendering the Projects Page
def render_projects(request):
    clients = Client.objects.all()
    projects = Project.objects.all()
    data = {
        "clients": clients,
        "projects": projects
    }
    return render(request, "admin_templates/projects.html", data)
# Add the Project to the databse
def add_projects(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    amount = request.POST.get("amount")
    clientname = request.POST.get("client name")
    startdate = request.POST.get("startdate")
    enddate = request.POST.get("enddate")
    client_obj = Client.objects.get(mainid=clientname)
    project_obj = Project(name=name, description=description, amount=amount, clientname=client_obj, startdate=startdate, duedate=enddate)
    project_obj.save()
    messages.success(request, "Project Added Successfully!")
    return HttpResponseRedirect(reverse("projects"))
# Rendering the Edit Projects Page
def edit_projects(request, mainid):
    project = Project.objects.get(mainid=mainid)
    clients = Client.objects.all()
    context = {
        "project": project,
        "projectid": mainid,
        "clients": clients
    }
    return render(request, "admin_templates/edit_projects.html", context=context)
# Rendering the More Information Page
def view_projects(request, mainid):
    project = Project.objects.get(mainid=mainid)
    context = {
        "project": project,
        "projectid": mainid
    }
    return render(request, "admin_templates/view_projects.html", context=context)
# Rendering the Delete projects Page
def delete_projects(request, mainid):
    project = Project.objects.get(mainid=mainid)
    context = {
        "project": project,
        "projectid": mainid
        
    }
    return render(request, "admin_templates/delete_projects.html", context=context)

# Performing the operation of editing a project
def edit_project(request):
    mainid = request.POST.get("mainid")
    name = request.POST.get("name")
    description = request.POST.get("description")
    amount = request.POST.get("amount")
    clientid = request.POST.get("clientname")
    
    client_obj = Client.objects.get(mainid=clientid)
    startdate= request.POST.get("startdate")
    duedate= request.POST.get("enddate")
    print(startdate)
    project_obj = Project.objects.get(mainid=mainid)
    project_obj.name = name
    project_obj.description = description
    project_obj.amount = amount
    project_obj.clientname = client_obj 
    project_obj.startdate = startdate
    project_obj.duedate = duedate 
    project_obj.save()
    messages.success(request, "Project Edited Successfully!")
    return HttpResponseRedirect(reverse("projects"))


# Performing the operation of deleting a project
def delete_project(request):
    mainid = request.POST.get("mainid")
    project_obj = Project.objects.get(mainid= mainid)
    project_obj.delete()
    messages.success(request, "Project Deleted Successfully!")
    return HttpResponseRedirect(reverse("projects"))
