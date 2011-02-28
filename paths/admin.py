from paths.models import Path, Blob
from django.contrib import admin

class BlobInLine(admin.TabularInline):
  model = Blob
  extra = 5

class PathAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Author',    {'fields':['auth_fname','auth_lname','auth_email']}),
    ('Path Information', {'fields':['nick','title','pub_date']}),
  ]
  inlines = [BlobInLine]
  list_display = ('title','pub_date','auth_name')
  list_filter = ['pub_date']
  search_fields = ['auth_name','pub_date','nick']
  date_hierarchy = 'pub_date'

admin.site.register(Path, PathAdmin)

