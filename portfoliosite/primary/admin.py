from django.contrib import admin
from .models import Contact

# Register your models here.



admin.site.site_header = "Erik's Profile Website";
admin.site.site_title = "Erik's Profile Website";

class ContactAdmin(admin.ModelAdmin):
    fields = ['Name', 'Email', 'Message', 'created_date']
    list_display = ('Name', 'Email', 'created_date')
    
admin.site.register(Contact, ContactAdmin)
