from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path(r'^', include('dogs.urls')),
    path(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path(r'^admin/', admin.site.urls),
]
