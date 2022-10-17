from django.contrib import admin
from .models import Application
# Register your models here.
#admin.site.register(Application)

# Register your models here.


class ApplicationAdmin(admin.ModelAdmin):
    @admin.action(description='Print Application')
    def generatePDF(modeladmin, request, queryset):
        url = 'templates/admin/application/?pks=' + ','.join(str([q.pk for q in queryset]))

    actions = [generatePDF]

admin.site.register(Application, ApplicationAdmin)
