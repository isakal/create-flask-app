from flask import Blueprint


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def page_not_found(error):
    return {"error_code": "404",
            "error": "Page not found."}, 404


@errors.app_errorhandler(403)
def access_denied(error):
    return {"error_code": "403",
            "error": "Access denied."}, 403


@errors.app_errorhandler(500)
def internal_error(error):
    return {"error_code": "500",
            "error": "Internal server error."}, 500
