import uuid
from http import HTTPStatus
from flask.views import MethodView
from flask_smorest import Blueprint
from api.dataBase.schemas import HomeMessageSchema, ErrorMessageSchema
from flask import current_app

# Blueprint in Flask Smorest would divide API in multiple segment
blp = Blueprint("home", __name__, url_prefix='/home', description="Here is my home/main page")

@blp.route("/")
class HomePage(MethodView):

    @blp.response(200, HomeMessageSchema)
    @blp.alt_response(HTTPStatus.INTERNAL_SERVER_ERROR, schema=ErrorMessageSchema)
    def get(self):
        try:
            return {"code": 200, "status": "success", "message": "Hello guys", "errors": {}}

        except Exception as e:
            current_app.logger.exception(f"An unexpected error occurred in file: {__file__}, error message: {e}")
            current_app.logger.info(f"STH WRONG IN FILE {__file__}")

            response_body = {
                "code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "status": "error",
                "message": str(e),
                "errors": {"detail": "Additional error details"}
            }

            return response_body, HTTPStatus.INTERNAL_SERVER_ERROR

