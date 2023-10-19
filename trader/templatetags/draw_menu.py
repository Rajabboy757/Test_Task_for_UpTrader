from django import template

from trader.models import Menu

register = template.Library()


@register.inclusion_tag('trader/menu.html', takes_context=True)
def draw_menu(context, name):
    menu = []

    if name == 'main_menu':
        menu_queryset = Menu.objects.all().select_related('parent')
        for item in menu_queryset:
            if item.is_main:
                menu.append(item)
    else:
        menu_queryset = context['menu_queryset']
        for item in menu_queryset:
            if item.parent and item.parent.name == name:
                menu.append(item)
    menu_id = context['menu_id']

    return {'menu_queryset': menu_queryset, 'menu': menu, 'menu_id': menu_id}
