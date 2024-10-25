from django.contrib import admin
from .models import CustomUser, Profissional, Consulta

admin.site.register(CustomUser)
admin.site.register(Profissional)
admin.site.register(Consulta)
