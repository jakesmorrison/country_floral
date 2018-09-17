from django.db import models

# Create your models here.

class Floral(models.Model):
    order_number = models.IntegerField(default=000, unique=True)

    delivered = models.BooleanField(default=False)

    date_processed = models.DateField(default="0000-00-00")
    time_processed = models.TimeField(default="00:00:00")

    customer_first_name = models.CharField(max_length=100, default="x")
    customer_last_name = models.CharField(max_length=100, default="x")
    customer_email = models.CharField(max_length=100, default="x")
    customer_phone = models.CharField(max_length=15, default="x")
    customer_instagram = models.CharField(max_length=100, default="x")

    recipient_name = models.CharField(max_length=100, default="x")
    recipient_phone = models.CharField(max_length=15, default="x")
    delivery_address = models.CharField(max_length=100, default="x")
    delivery_date = models.DateField(default="0000-00-00")
    delivery_type = models.CharField(max_length=100, default="x")
    del_name = models.CharField(max_length=100, default="x")

    delivery_message = models.TextField(max_length=500, default="x")

    design_keywords = models.TextField(max_length=1000, default="x")

    floral_cost = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    delivery_fee = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    total_cost = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(self.order_number,self.delivered,self.date_processed,self.time_processed,
                                                                     self.customer_first_name,self.customer_last_name,self.customer_email,self.customer_phone,self.customer_instagram,
                                                                     self.recipient_name,self.recipient_phone,self.delivery_address,self.delivery_date,
                                                                     self.delivery_message,self.design_keywords,self.floral_cost,self.delivery_fee, self.del_name, self.total_cost)
