from django.contrib import admin
from django.db.models.deletion import CASCADE
from . models import Slider,About,Apply,Fall,Featured,Teacher,Image,Store,Our,Basic,Make,Related

# Register your models here.

admin.site.register(Slider)
admin.site.register(About)
admin.site.register(Apply)
admin.site.register(Fall)
admin.site.register(Featured)
admin.site.register(Teacher)
admin.site.register(Image)
admin.site.register(Store)
admin.site.register(Our)
admin.site.register(Basic)
admin.site.register(Make)
admin.site.register(Related)

