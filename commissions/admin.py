from django.contrib import admin

from .models import CommissionType, Commission


class CommissionTypeAdmin(admin.ModelAdmin):
    model = CommissionType
    list_display = ("name",)
    search_fields = ('name',)

    fieldsets = [
        ('Details', {
            'fields': [
                'name',
                'description',
            ]
        })
    ]


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ("title", "people_required", "created_on", "updated_on",)
    search_fields = ('title',)
    list_filter = ('created_on',)

    fieldsets = [
        ('Details', {
            'fields': [
                'title',
                'description',
                'people_required',
            ]
        }),
    ]


admin.site.register(CommissionType, CommissionTypeAdmin)
admin.site.register(Commission, CommissionAdmin)
