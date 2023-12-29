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
def check_list_get_by_id(check_list_id):
    return check_lists_controller.check_list_get_by_id(request, check_list_id)


@check_lists.route("/check-list/<user_id>", methods=['GET'])
def check_list_get_by_user_id(user_id):
    return check_lists_controller.check_list_get_by_user_id(request, user_id)


@check_lists.route("/check-list/<check_list_id>", methods=['DELETE'])
def check_list_delete(check_list_id):
    return check_lists_controller.check_list_delete(request, check_list_id)