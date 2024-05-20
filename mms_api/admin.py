from django.contrib import admin
from .models import (Container)
from django.utils.html import format_html


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    def formatted_total_price_dinar(self, obj):
        return format_html(f"IQD {obj.total_dinar:,.0f}")

    def formatted_total_price_dollar(self, obj):
        return format_html(f"$ {obj.total_dollar:,.0f}")

    formatted_total_price_dinar.short_description = 'Total Dinar'  # Sets the column header
    # Sets the column header
    formatted_total_price_dollar.short_description = 'Total Dollar'

    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ['name']  # Fields to search by
    list_display = ['name', 'formatted_total_price_dinar', 'formatted_total_price_dollar',
                    'created_at', 'created_by']

    def get_actions(self, request):
        actions = super(ContainerAdmin, self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
