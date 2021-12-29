from django.contrib import admin
from mvtapp.models import webdevelopment_details

# Register your models here.
class webdevelopment_detailsAdmin(admin.ModelAdmin):
	list_display=('did','name','age','phone_no','gender')
admin.site.register(webdevelopment_details,webdevelopment_detailsAdmin)

 