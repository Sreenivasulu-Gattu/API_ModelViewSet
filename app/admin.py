from django.contrib import admin

# Register your models here.
from app.models import *

class cust(admin.ModelAdmin):
    list_display = ['id','fname','frating','fprice']

admin.site.register(Food,cust)