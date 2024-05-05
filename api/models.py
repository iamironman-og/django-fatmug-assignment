from django.db import models
from django.db.models import Avg
from django.utils import timezone


class Vendor(models.Model):

    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name


class PurchaseOrderManager(models.Manager):

    def calculate_on_time_delivery_rate(self, vendor):
        completed_pos = self.filter(vendor=vendor, status='completed')
        on_time_delivered_pos = completed_pos.filter(delivery_date__lte=timezone.now())
        total_completed_pos = completed_pos.count()
        if total_completed_pos == 0:
            return 0
        return on_time_delivered_pos.count() / total_completed_pos

    def update_quality_rating_average(self, vendor):
        completed_pos = self.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
        quality_rating_avg = completed_pos.aggregate(avg_rating=Avg('quality_rating'))['avg_rating']
        if quality_rating_avg is None:
            return 0
        return quality_rating_avg

    def calculate_average_response_time(self, vendor):
        acknowledged_pos = self.filter(vendor=vendor, acknowledgment_date__isnull=False)
        response_times = (pos.acknowledgment_date - pos.issue_date for pos in acknowledged_pos)
        response_time_total = sum(response_times, timezone.timedelta())
        if acknowledged_pos.count() == 0:
            return timezone.timedelta()
        return response_time_total / acknowledged_pos.count()

    def calculate_fulfillment_rate(self, vendor):
        total_pos = self.filter(vendor=vendor)
        successfully_fulfilled_pos = total_pos.filter(status='completed', quality_rating__isnull=True)
        if total_pos.count() == 0:
            return 0
        return successfully_fulfilled_pos.count() / total_pos.count()


class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    po_number = models.CharField(max_length=50, unique=True)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    objects = PurchaseOrderManager()

    def __str__(self):
        return self.po_number


# class VendorPerformanceRecord(models.Model):
class HistoricalPerformance(models.Model):
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
