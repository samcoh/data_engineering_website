from django.contrib import admin

# Register your models here.
from catalog.models import People, Project, Minor, Major, Section, People_Project, People_Minor, People_Major

#admin.site.register(People)
@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', "year_in_school", "role", "email")
    list_filter = ("last_name", "first_name", "role")
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','start_date', "end_date")
    list_filter = ("name", "start_date", "end_date")
admin.site.register(Minor)
admin.site.register(Major)
admin.site.register(Section)
admin.site.register(People_Project)
admin.site.register(People_Minor)
admin.site.register(People_Major)
