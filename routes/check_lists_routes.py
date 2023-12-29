from flask import request, Blueprint

from controllers import check_lists_controller

check_lists = Blueprint('check_lists', __name__)


@check_lists.route("/check-list", methods=['POST'])
def check_list_add():
    return check_lists_controller.check_list_add(request)


@check_lists.route("/check-lists", methods=['GET'])
def check_lists_get_all():
    return check_lists_controller.check_lists_get_all(request)


@check_lists.route("/check-list/<check_list_id>", methods=['GET'])
def check_list_get_by_id():
    return check_lists_controller.check_list_get_by_id(request)


@check_lists.route("/check-lists", methods=['GET'])
def check_list_get_by_user_id():
    return check_lists_controller.check_list_get_by_user_id(request)


@check_lists.route("/check-list/<check_list_id>", methods=['DELETE'])
def check_list_delete():
    return check_lists_controller.check_list_delete(request)