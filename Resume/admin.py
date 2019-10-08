from django.contrib import admin
from .models import Information,Education,Skills,Contact,Work_Experience

# Register your models here.
admin.site.register(Information)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Contact)
admin.site.register(Work_Experience)