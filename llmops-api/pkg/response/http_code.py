#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/6 10:09
@Author  : lianyutian
@File    : http_code.py
"""

from enum import Enum


class HttpCode(str, Enum):
    """HTTP基础业务状态码"""
    SUCCESS = 'success'  # 成功状态
    FAIL = 'fail'  # 失败状态
    NOT_FOUNT = 'not_fount'  # 未找到
    VALIDATION_ERROR = 'validation_error'  # 参数校验错误
