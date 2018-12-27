from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from .forms import *
import pandas as pd
from django.contrib.auth.decorators import login_required


def index(requests):
    return render(requests, 'index.html')


def add_new(requests):
    return render(requests, 'add_new.html')


def login(requset):
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
            return render(requset, 'index.html',{
                'message': ''
            })
        else:
            return render(requset, 'index.html', {
                'message': 'Username or Password is invalid',
                'error': True
            })

    else:
        return redirect('/')


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


def add_component_1(requests):
    if requests.method == 'GET':
        return render(requests, 'wizard.html')
    elif requests.method == 'POST':
        pass


def add_component_2(requests):
    if requests.method == 'GET':
        return render(requests, 'first_step.html')
    elif requests.method == 'POST':
        pass


def add_component_3(requests):
    if requests.method == 'GET':
        return render(requests, 'first_step.html')
    elif requests.method == 'POST':
        pass


def add_environment(requests):
    if requests.method == 'GET':
        return render(requests, 'add_environment.html')
    elif requests.method == 'POST':
        pass


def add_service(requests):
    if requests.method == 'GET':
        return render(requests, 'add_service.html')
    elif requests.method == 'POST':
        pass


def upload_backend_code(requests):
    if requests.method == 'GET':
        return render(requests, 'code-editor.html')
    elif requests.method == 'POST':
        pass


def analytics(request):
    if request.method == 'GET':
        return render(request, 'line-charts.html')