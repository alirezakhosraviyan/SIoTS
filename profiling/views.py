from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *
import pandas as pd
from django.contrib.auth.decorators import login_required
import json, random

@login_required
def index(requests):
    return render(requests, 'index.html')


def my_login(requset):
    if requset.method == 'GET':
        return render(requset, 'login-register.html')
    if requset.method == 'POST':
        form = LoginForm(requset.POST)
        if form.is_valid():
            username = str(form.cleaned_data['username'])
            password = str(form.cleaned_data['password'])
        else:
            return render(requset, 'index.html', {
                'message': form.errors,
                'error': True
            })

        user = authenticate(username=username, password=password)
        if user is not None:
            login(requset, user)
            return redirect('/')
        else:
            return render(requset, 'index.html', {
                'message': 'Username or Password is invalid',
                'error': True
            })

    else:
        return redirect('/')


def knapSack(W, wt, val, n):
    x1 = W + 1
    x2 = len(val)
    K = [[0 for x in range(x1)] for y in range(x2+1)]
    for index in range(1,len(val)+1):
        for weight in range(x1):
            if wt[index-1] > weight:
                K[index][weight] = K[index - 1][weight]
                continue
            prior_value = K[index - 1][weight]
            new_opion_best = val[index-1] + K[index - 1][weight - wt[index-1]]
            K[index][weight] = max(prior_value, new_opion_best)

    element = list()
    dp = K
    w = n
    i = W

    while (w > -1):
        if dp[w][i] == dp[w - 1][i] or w==0:
            w = w - 1
        else:
            element.append(w)
            i = i - wt[w-1]
            w = w - 1
    return element


def test(requests):
    if requests.method == 'GET':

        for cur in range(1, 5):
            u = User()
            u.save()
            d = DeviceType(type_name=random.randint(1, 17))
            d.save()
            Device(
                user=u,
                type=d
            ).save()
        devices = Device.objects.all()
        wt = [cur.evaluator() for cur in devices]
        val = [cur.weight for cur in devices]
        w = 100
        n = len(val)
        print(w,wt,val,n)
        res = knapSack(w, wt, val, n)
        print(res)
        for cur in Device.objects.all():
            cur.delete()
        for cur in User.objects.all():
            cur.delete()
        for cur in DeviceType.objects.all():
            cur.delete()

        return HttpResponse(res)


@login_required
def import_excel(requests):
    if requests.method == 'GET':
        return render(requests, 'import.html')
    elif requests.method == 'POST':
        try:
            file = ExcelFile(file=requests.FILES['file'])
            file.save()
            df = pd.read_csv(file.file.path)
            for index, row in df.iterrows():
                cur = row.values
                if len(cur) == 5:
                    device = Device()
                    device.pk = int(cur[0])
                    user, created = User.objects.get_or_create(pk=cur[1])
                    device.user = user
                    device_type, created = DeviceType.objects.get_or_create(pk=cur[2])
                    device.type = device_type
                    device.brand = int(cur[3])
                    device.model = int(cur[4])
                    device.save()
            return redirect('/all_devices/')
        except Exception as e:
            print(e)
            return HttpResponse(str(e))
    else:
        redirect('/404')


@login_required
def import_excel_location(requests):
    if requests.method == 'GET':
        return render(requests, 'import.html')
    elif requests.method == 'POST':
        try:
            file = ExcelFile(file=requests.FILES['file'])
            file.save()
            df = pd.read_csv(file.file.path)
            for index, row in df.iterrows():
                cur = row.values
                if len(cur) == 3:
                    if Device.objects.filter(pk=cur[0]).exists():
                        device = Device.objects.get(pk=cur[0])
                        device.long = cur[2]
                        device.lat = cur[1]
                        device.save()
            return redirect('/all_devices')
        except Exception as e:
            print(e)
            return HttpResponse(str(e))
    else:
        redirect('/404')


@login_required
def add_environment(requests):
    if requests.method == 'GET':
        return render(requests, 'add_environment.html', {'devices': Device.objects.all()})
    elif requests.method == 'POST':
        env = Environment(
            name=requests.POST['environment_name'],
            lat=requests.POST['lat'],
            long=requests.POST['long'],
        )
        env.save()
        for cur in requests.POST['available_services']:
            env.devices.add(Device.objects.get(id=cur))
        env.save()
        return redirect('/maps')


@login_required
def add_service(requests):
    if requests.method == 'GET':
        return render(requests, 'add_service.html')
    elif requests.method == 'POST':
        service = Service(
            name=requests.POST['service_name']
        )
        service.save()
        return redirect('/add_device')


@login_required
def add_device(requests):
    if requests.method == 'GET':
        return render(requests, 'add_device.html', {
            'users': User.objects.all(),
            'services': Service.objects.all(),
            'device_type': DeviceType.objects.all()
        })
    elif requests.method == 'POST':
        device = Device(
            brand=requests.POST['brand'],
            model=requests.POST['model'],
            lat=requests.POST['lat'],
            long=requests.POST['long'],
            user=User.objects.get(pk=requests.POST['user']),
            type=DeviceType.objects.get(pk=requests.POST['device_type']),
        )
        device.save()
        for cur in requests.POST['available_services']:
            device.services.add(Service.objects.get(pk=cur))

        device.save()
        return redirect('/add_environment')


@login_required
def all_services(requests):
    if requests.method == 'GET':
        return render(requests, 'all_services.html', {
            'services': Service.objects.all()
        })


@login_required
def all_devices(requests):
    if requests.method == 'GET':
        return render(requests, 'all_devices.html', {
            'devices': Device.objects.exclude(lat='')
        })


@login_required
def maps(requests):
    if requests.method == 'GET':

        device = Device.objects.exclude(lat__exact='')
        res = json.dumps([{'lat': float(cur.lat), 'lng': float(cur.long)} for cur in device])
        return render(requests, 'google-map.html', {
            'markers': res
        })



@login_required
def all_environments(requests):
    if requests.method == 'GET':
        return render(requests, 'all_environment.html', {
            'envs': Environment.objects.all()
        })


@login_required
def upload_backend_code(requests):
    if requests.method == 'GET':
        return render(requests, 'code-editor.html')
    elif requests.method == 'POST':
        pass


@login_required
def analytics(request):
    if request.method == 'GET':
        return render(request, 'line-charts.html')