from django.contrib import admin

from .models import MasterProfile, ParticipantProfile
# Register your models here.


class MasterAdmin(admin.ModelAdmin):

    class Meta:
        model = MasterProfile

admin.site.register(MasterProfile, MasterAdmin)
admin.site.register(ParticipantProfile)