from django.contrib import admin

# Register your models here.
from papers.models import Category, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass