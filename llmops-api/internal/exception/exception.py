#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/7 10:34
@Author  : lianyutian
@File    : exception.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode


class CustomException(Exception):
    """
    自定义异常基类
    """
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomException):
    """
    通用失败异常
    """
    pass


class NotFoundException(CustomException):
    """数据未查询到异常"""
    code = HttpCode.NOT_FOUNT


class ValidationException(CustomException):
    """数据验证异常"""
    code = HttpCode.VALIDATION_ERROR
