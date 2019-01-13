from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *
import pandas as pd
from django.contrib.auth.decorators import login_required


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

@login_required
def import_excel(requests):
    if requests.method == 'GET':

        return render(requests, 'import.html')
    elif requests.method == 'POST':
        form = ExcelFileForm(requests.POST, requests.FILES)

        if form.is_valid():
            try:
                form.save()
                file = ExcelFile.objects.last()
                df = pd.read_csv(file=file)
                for index, row in df.iterrows():
                    cur = str(row.values[0]).split(',')
                    print(cur)

                return
                df = pd.read_csv("objects_description.csv", "objects_description")
                for index, row in df.iterrows():
                    cur = str(row.values[0]).split(',')
                    if len(cur) == 5:
                        print(2)
                        device = Device()
                        device.pk = cur[0]
                        user, created = User.objects.get_or_create(pk=cur[1])
                        device.user = user
                        device.type = cur[2]
                        device.brand = cur[3]
                        device.model = cur[4]
                        device.save()
                    break
                return redirect('/app/motosel_manager/backend/')
            except Exception as e:
                return HttpResponse(str(e))
        else:
            return HttpResponse(str(form.errors))
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
        return redirect('/all_envs')


@login_required
def add_service(requests):
    if requests.method == 'GET':
        return render(requests, 'add_service.html')
    elif requests.method == 'POST':
        service = Service(
            name=requests.POST['service_name']
        )
        service.save()
        return redirect('/add_services')


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
        return redirect('/add_devices')

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
            'devices': Device.objects.all()
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