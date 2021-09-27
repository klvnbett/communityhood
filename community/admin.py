from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Neighbourhood)
admin.site.register(Health,HealthAdmin)
admin.site.register(Business)
admin.site.register(Healthservices)
admin.site.register(Authorities)
admin.site.register(BlogPost)
admin.site.register(Profile)
admin.site.register(Notifications)