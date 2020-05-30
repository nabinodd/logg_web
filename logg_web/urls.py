from django.contrib import admin
from django.urls import path
from io_handlr.views import (data_entry)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',data_entry)
]

urlpatterns+=staticfiles_urlpatterns()