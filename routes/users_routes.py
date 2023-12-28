from flask import request, Blueprint

from controllers import users_controller

user = Blueprint('user', __name__)


@user.route('/user', methods=['POST'])
def user_add():
    return users_controller.user_add(request)


@user.route('/users', methods=['GET'])
def users_get_all():
    return users_controller.users_get_all(request)


@user.route('/user/<user_id>', methods=['GET'])
def user_get_by_id():
    return users_controller.user_get_by_id(request)


@user.route('/user/<user_id>', methods=['PUT'])
def user_update():
    return users_controller.user_update(request)


@user.route('/user/activity/<user_id>', methods=['PATCH'])
def user_activity():
    return users_controller.user_activity(request)


@user.route('/user/delete/<user_id>', methods=['DELETE'])
def user_delete():
    return users_controller.user_delete(request)

