from flask import request, Blueprint

from controllers import users_controller

user = Blueprint('user', __name__)


@user.route('/user', methods=['POST'])
def user_add():
    return users_controller.user_add(request)


@user.route('/users', methods=['GET'])
def users_get_all():
    return users_controller.users_get_all(request)


@user.route('/user/activity/<user_id>', methods=['PATCH'])
def user_activity():
    return users_controller.user_activity(request)

