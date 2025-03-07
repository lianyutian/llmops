#!/user/bin/.env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/4 16:14
@Author  : lianyutian
@File    : http.py
"""
from flask import Flask

from config import Config
from internal.exception.exception import CustomException
from internal.router import Router
from pkg.response import json, Response, HttpCode


class Http(Flask):
    """http服务引擎"""

    def __init__(self, *args, config: Config, route: Router, **kwargs):
        super().__init__(*args, **kwargs)
        route.register_router(self)

        self.register_error_handler(Exception, self._register_error_handler)

        self.config.from_object(config)

    def _register_error_handler(self, error: Exception):
        """注册错误处理"""
        if isinstance(error, CustomException):
            return json(
                Response(code=error.code, message=error.message, data=error.data if error.data is not None else {}))
        if self.debug:
            raise error
        else:
            return json(Response(code=HttpCode.FAIL, message=str(error)))
