# coding=utf-8
CONFIGURATION_IS_INVALID = '001001'

API_EXCEPTION = '002001'
TOKEN_INVALID = '002002'
LOGIN_NEEDED = '002003'
KEY_INVALID = '002004'
INVALID_PARAM = '002005'
INVALID_ORDER_ID = '002006'
TRANSPORT_EXCEPTION = '002007'


class SnbException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg


class ConfigException(SnbException):
    """
    配置文件错误
    """
    pass


class ApiExecuteException(SnbException):
    """
    API 业务错误
    """
    pass


class TokenInvalid(SnbException):
    """
    Token 过期 或 无效
    """
    pass


class InvalidParamException(SnbException):
    """
    API 入参
    """
    pass


class ApiTransportException(SnbException):
    """
    网络错误
    """
    pass
