from django.contrib import admin

# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


class PartnerAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)