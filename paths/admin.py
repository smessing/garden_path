from paths.models import Path, Blob
from django.contrib import admin

class BlobInLine(admin.TabularInline):
  model = Blob
  extra = 5

class PathAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Author',    {'fields':['auth_fname','auth_lname','auth_email']}),
    # ('Approval Status', {'fields':['approval']}),
    ('Path Information', {'fields':['nick','title','pub_date']}),
  ]
  inlines = [BlobInLine]

admin.site.register(Path, PathAdmin)

