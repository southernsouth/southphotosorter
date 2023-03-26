from django.contrib import admin
from django.urls import path
from photosorter import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
