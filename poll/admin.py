from django.contrib import admin

# Register your models here.
from .models import RandomImage,Question

admin.site.register(RandomImage)
admin.site.register(Question)
