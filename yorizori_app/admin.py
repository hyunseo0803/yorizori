from django.contrib import admin

# Register your models here.
from .models import MemberInfo, Recipe
admin.site.register(MemberInfo)
admin.site.register(Recipe)