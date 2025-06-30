from django.contrib import admin
from .models import Centre, ExpenseClaim, ClaimItem
# Register your models here.

admin.site.register(Centre)
admin.site.register(ExpenseClaim)
admin.site.register(ClaimItem)