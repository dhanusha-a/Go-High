from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomePage.urls')),
    path('contact/', include('HomePage.urls')),
    path('login/', include('registration.urls'))

]
