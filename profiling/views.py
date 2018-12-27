from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from .forms import *
import pandas as pd
from django.contrib.auth.decorators import login_required


def index(requests):
    return render(requests, 'index.html')


@login_required
def add_new(requests):
    return render(requests, 'add_new.html')


@login_required
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
def add_component(requests):
    if requests.method == 'GET':
        return render(requests, 'first_step.html')
    elif requests.method == 'POST':
        pass


@login_required
def upload_backend_code(requests):
    if requests.method == 'GET':
        return render(requests, '')
    elif requests.method == 'POST':
        pass
