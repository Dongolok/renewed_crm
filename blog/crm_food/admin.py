from django.contrib import admin
from .models import *
from registration.models import Roles, Users
# Register your models here.

admin.site.register(Meals)
admin.site.register(MealCategories)
admin.site.register(Departments)
admin.site.register(Orders)
admin.site.register(ServicePercentage)
admin.site.register(Tables)
admin.site.register(Check)
admin.site.register(Status)
admin.site.register(MealsToOrder)
admin.site.register(Roles)
admin.site.register(Users)
