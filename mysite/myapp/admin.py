from django.contrib import admin
from .models import Ambulance
from .models import Pharmacy
from .models import BloodBank
from .models import Hospital
# Register your models here.s

admin.site.register(Ambulance)
admin.site.register(Pharmacy)
admin.site.register(BloodBank)
admin.site.register(Hospital)
