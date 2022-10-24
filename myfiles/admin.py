from django.contrib import admin

# Register your models here.
from myfiles.models import *
class AdminService(admin.ModelAdmin):
    list_display = ['id','nomi','old_price','new_price','rasm','vaqt']

admin.site.register(Service,AdminService)


class AdminM(admin.ModelAdmin):
    list_display = ['id','ism','mail','subject','message','vaqt']

admin.site.register(Murojaat,AdminM)