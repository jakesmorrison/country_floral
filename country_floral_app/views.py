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
    cost = cfg.CONFIG.BASE_DEL_FEE
    try:
        params = request.GET
        url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + params["start"] + "&destination=" + \
              params["stop"] + "&key=AIzaSyAoLeCMmBMEkX7-UAwnbeWEWoQGLJSjFnI"
        url = url.replace(" ", "%20")
        response = urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(response.read().decode(encoding))
        distance = float((data["routes"][0]["legs"][0]["distance"]["text"]).split(" ")[0])

        if distance > 3:
            cost = cost + int(distance - 3) * .5

    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"addresss error: " + str(e))
        cost = 0

    context ={
        "cost": ("%.2f"%(cost)),
    }
    return JsonResponse(json.loads(json.dumps(context)))


def process(request):
    params = request.GET

    # Customer Information
    try:
        if params["fname"] == "":
            fname = "none"
        else:
            fname = params["fname"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"fname error: " + str(e))

    try:
        if params["lname"] == "":
            lname = "none"
        else:
            lname = params["lname"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"lname error: " + str(e))

    try:
        if params["email"] == "":
            email = "none"
        else:
            email = params["email"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"email error: " + str(e))

    try:
        if params["myphone"] == "":
            customer_phone = "none"
        else:
            customer_phone = params["myphone"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"customer_phone error: " + str(e))

    try:
        if params["instagram"] == "":
            instagram = "none"
        else:
            instagram = params["instagram"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"instagram error: " + str(e))


    # Recipient Information
    try:
        if params["recipient"] == "":
            recipient = "none"
        else:
            recipient = params["recipient"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"recipient error: " + str(e))

    try:
        if params["custphone"] == "":
            rec_phone_number = "none"
        else:
            rec_phone_number = params["custphone"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"rec_phone_number error: " + str(e))

    try:
        if params["address"] == "":
            address = "none"
        else:
            address = params["address"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"address error: " + str(e))

    try:
        if params["date"] == "":
            delivery_date = "none"
        else:
            delivery_date = params["date"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"delivery_date error: " + str(e))

    try:
        if params["message"] == "":
            message = "none"
        else:
            message = params["message"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"message error: " + str(e))


    # Design
    try:
        if params["keywords"] == "":
            keywords = "none"
        else:
            keywords = params["keywords"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"keywords error: " + str(e))


    # Cost
    try:
        if params["total"] == "":
            total = "none"
        else:
            total = params["total"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " +"total error: " + str(e))

    try:
        if params["delivery_fee"] == "":
            delivery_fee = "none"
        else:
            delivery_fee = params["delivery_fee"]
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " + "delivery_fee error: " + str(e))

    try:
        if params["user_input"] == "":
            user_input = "none"
        else:
            user_input = params["user_input"].replace("$","").replace("_","")
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " + "user_input error"  + str(e))


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


    my_error_string = time + " | " + date + " | " + fname + " | " + lname + " | " + email  + " | " + customer_phone  + " | " \
                      "" + recipient  + " | " +  rec_phone_number  + " | " + address  + " | " +  delivery_date  + " | " +  message  + " | " \
                      "" + keywords  + " | " + total  + " | " + delivery_fee

    write_to_error_file(my_error_string)
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # my_path = os.path.join(BASE_DIR, 'error_file.txt')
    # from django.conf import settings
    # os.path.join(settings.MEDIA_ROOT, 'error_file.txt')
    try:
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
            total_cost = float(total),
        )
        s.save()
    except Exception as e:
        write_to_error_file(time + " | " + date + " | " + "database error: " + str(e))

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

def write_to_error_file(error_string):
    try:
        with open("/root/database/error_file.txt", "a") as myfile:
            myfile.write(error_string + "\n")
    except:
        pass
