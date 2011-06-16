from django.contrib import admin
from ipauth.models import Range



class RangeAuth(admin.ModelAdmin):
    list_display = ('user', 'lower', 'upper',)
    search_fields = ('user__first_name', 'user__last_name', 'lower', 'upper',)

admin.site.register(Range, RangeAuth)