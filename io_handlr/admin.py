from django.contrib import admin
from .models import Visitor

class VisitorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Visitor,VisitorAdmin)
# Register your models here.
