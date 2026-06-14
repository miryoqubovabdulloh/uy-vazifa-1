from django.contrib import admin
from django.urls import path
from templatemo.views import templatemo,work,contact


urlpatterns = [
    path('', templatemo),
    path('work/', work),
    path('contact/', contact),
    path('admin/', admin.site.urls),
]
