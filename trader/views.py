from django.shortcuts import render

from .models import Menu


def show_menu(request, menu_id):

    data = {
        'menu_id': menu_id,
        'name': 'main_menu'
    }
    return render(request, 'trader/index.html', context=data)
