from flask import jsonify
from enum import Enum


class ResponseCode(Enum):
    """定义枚举类型表示响应码"""

    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404


class ResponseBuilder:
    @staticmethod
    def build_response(code, data=None, message=None):
        """
        构建响应数据

        参数:
            code (ResponseCode): 响应码
            data (any, optional): 响应数据，默认为None
            message (str, optional): 响应消息，默认为None

        返回:
            dict: 响应数据的字典形式
        """
        response = {"code": code.value, "data": data, "message": message}
        return jsonify(response)

    @staticmethod
    def build_success_response(data=None, message=None):
        """
        构建成功响应数据

        参数:
            data (any, optional): 响应数据，默认为None
            message (str, optional): 响应消息，默认为None

        返回:
            dict: 成功响应数据的字典形式
        """
        return ResponseBuilder.build_response(ResponseCode.OK, data, message)

    @staticmethod
    def build_error_response(code, message=None):
        """
        构建错误响应数据

        参数:
            code (ResponseCode): 错误响应码
            message (str, optional): 错误响应消息，默认为None

        返回:
            dict: 错误响应数据的字典形式
        """
        return ResponseBuilder.build_response(code, None, message)
