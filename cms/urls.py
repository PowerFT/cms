"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cmsapp import views, admin_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_home, name = 'home'),
    path('about/', views.render_about, name="about"),
    path('contact/', views.render_contact, name="contact"),
    path('login/', views.render_login, name="render_login"),
    path('signup/', views.render_signup, name="render_signup"),
    path("perform_login", views.perform_login, name="perform_login"),
    path("perform_logout", views.perform_logout, name="perform_logout"),
    
    #### Here starts the urls for the admin panel
    path("dashboard/", admin_views.render_dashboard, name="dashboard"),
    path("clients/", admin_views.render_clients, name="clients"),
    path("add_clients", admin_views.add_clients, name="add_clients"),
    path("edit_client", admin_views.edit_client, name="edit_client"),
    path("delete_client", admin_views.delete_client, name="delete_client"),
    path("edit_clients/<str:mainid>", admin_views.edit_clients, name="edit_clients"),
    path("view_clients/<str:mainid>", admin_views.view_clients, name="view_clients"),
    path("delete_clients/<str:mainid>", admin_views.delete_clients, name="delete_clients"),
    
    path("projects/", admin_views.render_projects, name="projects"),
    path("add_projects", admin_views.add_projects, name="add_projects"),
    path("edit_project", admin_views.edit_project, name="edit_project"),
    path("delete_project", admin_views.delete_project, name="delete_project"),
    path("edit_projects/<str:mainid>", admin_views.edit_projects, name="edit_projects"),
    path("view_projects/<str:mainid>", admin_views.view_projects, name="view_projects"),
    path("delete_projects/<str:mainid>", admin_views.delete_projects, name="delete_projects"),
    
]
