# Register your models here.
from django.contrib import admin
from .models import Page
# Register your models here.


class  PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

admin.site.register(Page,PageAdmin)