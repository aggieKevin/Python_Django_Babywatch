from django.contrib import admin
from .models import Household, Guardian,Child

admin.site.register(Household)
admin.site.register(Guardian)
admin.site.register(Child)

# Register your models here.
