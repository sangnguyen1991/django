
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('contact/', include('contact.urls')),
    path('user_auth/', include('user_auth.urls')),
    path('mymodel/', include('mymodel.urls')),
    path('admin/', admin.site.urls),
]
