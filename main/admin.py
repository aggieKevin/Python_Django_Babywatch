from django.contrib import admin
from .models import Household, Guardian,Child,Rating

admin.site.register(Household)
admin.site.register(Guardian)
admin.site.register(Child)
admin.site.register(Rating)

# Register your models here.
