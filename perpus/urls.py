from django.conf.urls import url
from django.contrib import admin
from perpustakaan.views import buku, penerbit

urlpatterns = [
    url('admin/', admin.site.urls),
    url('buku/', buku),
    url('penerbit/', penerbit),
]
