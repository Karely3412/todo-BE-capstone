from flask import request, Blueprint

from controllers import auth_tokens_controller

auth_token = Blueprint('auth_token', __name__)


@auth_token.route('/user/auth', methods=['POST'])
def auth_token_add():
    return auth_tokens_controller.auth_token_add(request)