from flask import request, Blueprint

from controllers import items_controller

items = Blueprint('items', __name__)


@items.route('/item', methods=['POST'])
def item_add():
    return items_controller.item_add(request)


@items.route('/items', methods=['GET'])
def item_get_all():
    return items_controller.item_get_all(request)


@items.route('/item/<item_id>', methods=['GET'])
def item_get_by_id(item_id):
    return items_controller.item_get_by_id(request, item_id)


@items.route('/item/<check_list_id>', methods=['GET'])
def item_get_by_check_list_id(check_list_id):
    return items_controller.item_get_by_check_list_id(request, check_list_id)


@items.route('/item/<item_id>', methods=['DELETE'])
def item_delete(item_id):
    return items_controller.item_delete(request, item_id)