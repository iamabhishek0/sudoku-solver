from django.contrib import admin
from django.urls import path
from sudokusolver.views import index, custom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('custom', custom, name="custom-solver"),
]
