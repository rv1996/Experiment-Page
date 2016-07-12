from django.contrib import admin

from .models import Experiment


# Register your models here.

class AdminExperiment(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp', 'updated']
    list_editable = ['title']
    list_display_links = ['updated']
    search_fields = ['title', 'content']
    list_filter = ['updated', 'timestamp']

    class Meta:
        model = Experiment


admin.site.register(Experiment, AdminExperiment)
