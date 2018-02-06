from django.contrib import admin
from .models import Hospital,Doctor,Patient,rtx_infusion,followup

# Register your models here.

admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(rtx_infusion)
admin.site.register(followup)
