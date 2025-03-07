#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/6 10:12
@Author  : lianyutian
@File    : response.py
"""
from dataclasses import field, dataclass
from typing import Any

from flask import jsonify

from pkg.response.http_code import HttpCode


@dataclass
class Response:
    """基础HTTP接口响应格式"""
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    """基础响应函数"""
    return jsonify(data), 200


def success_json(data: Any = None):
    """成功响应"""
    return json(Response(code=HttpCode.SUCCESS, data=data))


def fail_json(data: Any = None):
    """失败响应"""
    return json(Response(code=HttpCode.FAIL, data=data))


def validate_error_json(errors: dict = None):
    """验证失败响应"""
    first_key = next(iter(errors))
    if first_key is not None:
        print(first_key)
        msg = errors[first_key][0]
    else:
        msg = ""
    return json(Response(code=HttpCode.VALIDATION_ERROR, message=msg))
