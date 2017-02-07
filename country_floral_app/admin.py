from django.contrib import admin

# Register your models here.
class FloralModelAdmin(admin.ModelAdmin):
    list_display="order_number,self.delivered,self.date_processed,self.time_processed,self.customer_first_name, self.customer_last_name, self.customer_email,self.customer_phone, " \
                 "self.customer_instagram,self.recipient_name, self.recipient_phone, self.delivery_address, self.delivery_date," \
                 "self.delivery_message, self.design_keywords,self.floral_cost, self.delivery_fee, self.total_cost".replace(" ","").replace("self.", "").split(",")
    search_fields = list_display
from .models import Floral
admin.site.register(Floral, FloralModelAdmin)

