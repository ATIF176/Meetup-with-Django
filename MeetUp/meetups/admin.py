from django.contrib import admin

from .models import MeetUp, Location, Particicpant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(MeetUp, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Particicpant)
