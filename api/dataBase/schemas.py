from marshmallow import Schema, fields

class HomeMessageSchema(Schema):
    code = fields.Integer()
    status = fields.String()
    message = fields.String()
    errors = fields.Dict()

class ErrorMessageSchema(Schema):
    code = fields.Integer()
    status = fields.String()
    message = fields.String()
    errors = fields.Dict(allow_none=True)
