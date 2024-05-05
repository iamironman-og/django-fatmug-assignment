from django.contrib import admin
from .models import PurchaseOrder, Vendor, HistoricalPerformance
# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    pass


class PurchaseOrderAdmin(admin.ModelAdmin):
    pass


class HistoricalPerformanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vendor, VendorAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)
