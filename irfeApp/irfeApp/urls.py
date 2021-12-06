
from django.contrib import admin
from django.urls import path, include
#from django.urls.conf import include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('formations/', include('formations.urls')),
]
