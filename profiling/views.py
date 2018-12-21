from django.shortcuts import render


def index(requests):
    return render(requests, 'index.html')


def import_excel(requests):
    return render(requests, 'import.html')


def add_new(requests):
    return render(requests, 'add_new.html')