from django.contrib import admin
from pins.models import PinImage, Category, ImageHasCategory
# Register your models here.
admin.site.register(PinImage)
admin.site.register(Category)

class ImageHasCatgoryAdmin(admin.ModelAdmin):
    fields = ('pinImage', 'category')
    list_display = ('pinImage', 'category')
admin.site.register(ImageHasCategory, ImageHasCatgoryAdmin)
