from django.contrib import admin
from .models import Project, Review, Tag


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['value', 'created']
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)

