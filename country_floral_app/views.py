from django.shortcuts import render
from .management import config as cfg
from django.http import JsonResponse
import json
from urllib.request import urlopen

from datetime import datetime, timedelta
from pytz import timezone

from .models import Floral
import os

# Create your views here.

def index(request):
    context = {
    }
    return render(request, 'country_floral_app/index.html', context)

def order(request):
    keyword_list = []
    for x in cfg.CONFIG.KEYWORDS.values():
        keyword_list+=x
    context = {
        "keyword_list":cfg.CONFIG.KEYWORDS,
    }
    return render(request, 'country_floral_app/order.html', context)

def get_distance(request):
    params = request.GET
    url = "https://maps.googleapis.com/maps/api/directions/json?origin="+params["start"]+"&destination="+params["stop"]+"&key=AIzaSyAoLeCMmBMEkX7-UAwnbeWEWoQGLJSjFnI"
    url = url.replace(" ","%20")
    response = urlopen(url)
    encoding = response.info().get_content_charset('utf8')
    data = json.loads(response.read().decode(encoding))
    distance = float((data["routes"][0]["legs"][0]["distance"]["text"]).split(" ")[0])

    cost = cfg.CONFIG.BASE_DEL_FEE
    if distance > 3:
        cost = cost + int(distance - 3)*.5

    context ={
        "cost": ("%.2f"%(cost)),
    }
    return JsonResponse(json.loads(json.dumps(context)))


def process(request):
    params = request.GET

    # Customer Information
    fname = params["fname"]
    lname = params["lname"]
    email = params["email"]
    customer_phone = params["myphone"]
    instagram = params["instagram"]

    if instagram == "":
        instagram = "none"

    # Recipient Information
    recipient = params["recipient"]
    rec_phone_number = params["custphone"]
    address = params["address"]
    delivery_date = params["date"]
    message = params["message"]

    # Design
    keywords = params["keywords"]

    # Cost
    total = params["total"]
    delivery_fee = params["delivery_fee"]
    user_input = params["user_input"].replace("$","").replace("_","")

    # Time
    mountain = timezone('US/Mountain')
    mountain_time = datetime.now(mountain)
    date_time = mountain_time.strftime('%Y-%m-%d_%H:%M:%S').split("_")

    date = date_time[0]
    time = date_time[1]

    try:
        order_number = int(max(list(Floral.objects.values_list("order_number", flat=True)))+1)
    except:
        order_number = 0

    my_error_string = time + "\t" + date + "\t" + fname + "\t" + lname + "\t" + email  + "\t" + customer_phone  + "\t" \
                      "" + recipient  + "\t" +  rec_phone_number  + "\t" + address  + "\t" +  delivery_date  + "\t" +  message  + "\t" \
                      "" + keywords  + "\t" + total  + "\t" + delivery_fee


    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    my_path = os.path.join(BASE_DIR, 'error_file.txt')

    from django.conf import settings
    with open(os.path.join(settings.MEDIA_ROOT, 'error_file.txt'), "a") as myfile:
        myfile.write(my_error_string + "\n")


    s = Floral(
        order_number = order_number,
        delivered = False,
        date_processed = date,
        time_processed = time,
        customer_first_name = fname,
        customer_last_name = lname,
        customer_email = email,
        customer_phone = customer_phone,
        customer_instagram = instagram,
        recipient_name = recipient,
        recipient_phone = rec_phone_number,
        delivery_address = address,
        delivery_date = delivery_date,
        delivery_message = message,
        design_keywords = keywords,
        floral_cost = int(user_input),
        delivery_fee = float(delivery_fee),
        total_cost = float(total)
    )
    s.save()

    context ={
        "order_number": order_number,
    }
    return JsonResponse(json.loads(json.dumps(context)))
    # return render(request, 'country_floral_app/order.html', context)

def about(request):
    context = {
    }
    return render(request, 'country_floral_app/about.html', context)

def contact(request):
    context = {
    }
    return render(request, 'country_floral_app/contact.html', context)

def gallery(request):
    context = {
    }
    return render(request, 'country_floral_app/gallery.html', context)

def events(request):
    context = {
    }
    return render(request, 'country_floral_app/events.html', context)