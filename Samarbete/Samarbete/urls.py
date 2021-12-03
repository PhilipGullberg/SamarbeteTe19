
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Person 1, Använd include för att kopp tilla mainsite.urls, register.urls och shop.urls
    path('mainsite/', include('mainsite.urls')),
    path('register/', include('register.urls') ),
    path('shop/', include('shop.urls') ),
]
