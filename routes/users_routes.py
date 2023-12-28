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
def user_get_by_id(user_id):
    return users_controller.user_get_by_id(request, user_id)


@user.route('/user/<user_id>', methods=['PUT'])
def user_update(user_id):
    return users_controller.user_update(request, user_id)


@user.route('/user/activity/<user_id>', methods=['PATCH'])
def user_activity(user_id):
    return users_controller.user_activity(request, user_id)


@user.route('/user/delete/<user_id>', methods=['DELETE'])
def user_delete(user_id):
    return users_controller.user_delete(request, user_id)

