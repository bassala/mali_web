from django.contrib import admin
from .models import Bamako, Gao, Kidal, Koulikoro, Mopti, Ségou, Sikasso, Timbuktu,Kayes

# Pour Bamako
class BamakoAdmin(admin.ModelAdmin):
    list_display = ("habitats",)  

admin.site.register(Bamako, BamakoAdmin)

# Pour Gao
class GaoAdmin(admin.ModelAdmin):
    list_display = ("habitats",)  

admin.site.register(Gao, GaoAdmin)

# Pour Kidal
class KidalAdmin(admin.ModelAdmin):
    list_display = ("habitats",)  

admin.site.register(Kidal, KidalAdmin)

# Pour Koulikoro
class KoulikoroAdmin(admin.ModelAdmin):
    list_display = ("habitats",)  

admin.site.register(Koulikoro, KoulikoroAdmin)

# Pour Mopti
class MoptiAdmin(admin.ModelAdmin):
    list_display = ("habitats",)  

admin.site.register(Mopti, MoptiAdmin)

# Pour Ségou
class SegouAdmin(admin.ModelAdmin):
    list_display = ("habitats",)  

admin.site.register(Ségou, SegouAdmin)

# Pour Sikasso
class SikassoAdmin(admin.ModelAdmin):
    list_display = ("habitats",)  

admin.site.register(Sikasso, SikassoAdmin)

# Pour Timbuktu
class TimbuktuAdmin(admin.ModelAdmin):
    list_display = ("habitats",)  

admin.site.register(Timbuktu, TimbuktuAdmin)

# pour kayes
class kayesAdmin(admin.ModelAdmin):
    list_display = ("habitats",)  

admin.site.register(Kayes, kayesAdmin)

