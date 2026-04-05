from django.contrib import admin
from django.urls import path,include
from home import views 

#admin customization
admin.site.site_header="Dev's Portfolio Admin"
admin.site.site_title="Dev's Portfolio Admin Portal"
admin.site.index_title="Welcome to Dev's Portfolio Admin Portal"
urlpatterns = [
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contacts', views.contacts, name='contacts')
]
