from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from .models import County, Form, Port, Vessel, Passenger
from .forms import ParkingChangeForm, VesselChangeForm, PassengerChangeForm
from nfvpap.decorators import group_required
import json


def apply(request):
    # print(request.POST)
    counties = County.objects.all()
    ports = Port.objects.all()
    if request.method == 'POST':
        form_filling_date = request.POST.get('form_filling_date')
        scheduled_arrival = request.POST.get('scheduled_arrival')
        scheduled_departure = request.POST.get('scheduled_departure')
        purpose = request.POST.get('purpose')
        county = request.POST.get('county')
        port = request.POST.get('port')
        ship_name = request.POST.get('ship_name')
        tonnage = request.POST.get('tonnage')
        ship_size = request.POST.get('ship_size')
        ship_properties = request.POST.get('ship_properties')
        passenger = request.POST.get('passenger')
        person_name = request.POST.get('person_name')
        person_incharge = request.POST.get('person_incharge')
        id_num = request.POST.get('id_num')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        contact_no = request.POST.get('contact_no')
        mobile_no = request.POST.get('mobile_no')
        fax_no = request.POST.get('fax_no')
        cert = request.POST.get('cert')

        parking_form = Form()
        parking_form.form_filling_date = form_filling_date
        parking_form.scheduled_arrival = scheduled_arrival
        parking_form.scheduled_departure = scheduled_departure
        parking_form.purpose = purpose
        # parking_form.port = port
        
        # vessel_form = Vessel()
        # vessel_form.shipname = ship_name
        # vessel_form.tonnage = tonnage
        

        # parking_form = ParkingChangeForm(request.POST)
        # vessel_form = VesselChangeForm(request.POST)
        # passenger_form = PassengerChangeForm(request.POST)
   
        # if parking_form.is_valid() and vessel_form.is_valid() and passenger_form.is_valid():
        #     parking_form.save()
        #     vessel_form.save()
        #     passenger_form.save()
        #     messages.success(request, '已送出申請')
        

    return render(request, 'parking/apply.html', {
        'counties': counties,
        'ports': ports,
        # 'parking_form': parking_form,
        # 'vessel_form': vessel_form,
        # 'passenger_form': passenger_form,
    })

def load_ports(request):
    county_id = request.GET.get('county')
    ports = Port.objects.filter(county_id=county_id)
    return render(request, 'parking/port_dropdown_list_options.html', {'ports': ports})

def load_vessels(request):
    ship_name = request.GET.get('ship_name')
    ship = Vessel.objects.get(shipname=ship_name)
    ship_properties_mapping = {
        '工作船' : 'working',
        '交通船' : 'traffic',
        '海上遊樂船舶' : 'recreation',
        '公務船舶、研究船、訓練船' : 'official',
        '國內新建造之銷售用遊艇' : 'yacht',
    }
    data = {
        'ship_name': ship.shipname,
        'tonnage': ship.tonnage,
        'length': ship.length,
        'properties': ship_properties_mapping[ship.ship_kind],
    }
    return JsonResponse(data)

def history(request):
    return render(request, 'parking/history.html')

def payment(request):
    return render(request, 'parking/payment.html')

def calculate_payment(request):
    return render(request, 'parking/calculate_payment.html')

def payment_admin(request):
    return render(request, 'parking/payment_admin.html')

def payment_refund(request):
    return render(request, 'parking/payment_refund.html')

def parkings(request):
    return render(request, 'parking/parkings.html')

def not_applied(request):
    return render(request, 'parking/not_applied.html')

def not_applied_review(request):
    print('review')
    return render(request, 'parking/not_applied_review.html')

# @group_required('海巡署')
def review(request):
    return render(request, 'parking/review.html')
    
def berth_review(request):
    return render(request, 'parking/berth_review.html')

def berth_view(request):
    return render(request, 'parking/berth_view.html')

def statistics(request):
    return render(request, 'parking/statistics.html')

def admin_apply(request):
    return render(request, 'parking/apply.html')

def new_edit(request):
    return render(request, 'parking/new_edit.html')

def news_list(request):
    return render(request, 'parking/news_list.html')

def create_new(request):
    return render(request, 'parking/create_new.html')
    
def add_new_type(request):
    return render(request, 'parking/add_new_type.html')

def add_nocharge_reason(request):
    reasons = ['緊急避難', '無害通過', '進港不停泊']
    return render(request, 'parking/add_nocharge_reason.html', {
        'reasons': reasons,
    })

def refund(request):
    return render(request, 'parking/refund.html')