from django.contrib import admin
from .models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name', 'phone','show',)
    list_display_links = ('id', 'first_name',)
    ordering = ('-id',)
    search_fields = ('first_name', 'last_name',)
    list_filter = 'created_date',
    list_editable = ('show',)
    list_per_page=10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= 'name',