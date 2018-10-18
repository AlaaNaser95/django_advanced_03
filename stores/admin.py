from django.contrib import admin
from .models import Store

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
	list_display = ('name','id', 'description')
	list_filter = ['added']
	search_fields = ['name','description']
	list_editable=['description']
admin.site.register(Store, StoreAdmin)