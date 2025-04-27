from django import template
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('webinterface/menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_slug):
    try:
        menu_items = MenuItem.objects.filter(menu__slug=menu_slug)

        current_path = context['request'].path

        active_item = None
        for item in menu_items:
            item_url = item.get_url()
            if item_url == current_path:
                active_item = item
                break

        root_items = []
        for item in menu_items:
            if item.parent is None:
                root_items.append(item)

        active_item_ids = []
        if active_item:
            current = active_item
            while current:
                active_item_ids.append(current.id)
                current = current.parent

        return {
            'menu': menu_slug,
            'root_items': root_items,
            'active_item_ids': active_item_ids,
            'menu_items': menu_items,
            'request': context['request'],
        }
    except Menu.DoesNotExist:
        return {'menu': None}


@register.simple_tag
def is_active(item, active_item_ids):
    return item.id in active_item_ids


@register.simple_tag
def has_active_child(item, active_item_ids, all_items):
    for child in all_items:
        if child.parent_id == item.id and child.id in active_item_ids:
            return True
    return False