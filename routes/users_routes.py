from flask import request, Blueprint

from controllers import users_controller

user = Blueprint('user', __name__)


@user.route('/user/add', methods={'POST'})
def user_add():
    return users_controller.user_add()