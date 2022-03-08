from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Park, Coaster

class ParkResource(resources.ModelResource):
  class Meta:
      model = Park

class ParkAdmin(ImportExportModelAdmin):
    resource_class = ParkResource

class CoasterResource(resources.ModelResource):
  class Meta:
    model = Coaster
class CoasterAdmin(ImportExportModelAdmin):
  resource_class = CoasterResource


admin.site.register(Park, ParkAdmin)
admin.site.register(Coaster, CoasterAdmin)
