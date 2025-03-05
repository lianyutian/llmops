#!/user/bin/.env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/4 16:14
@Author  : lianyutian
@File    : http.py
"""
from flask import Flask

from config import Config
from internal.router import Router


class Http(Flask):
    """http服务引擎"""

    def __init__(self, *args, config: Config, route: Router, **kwargs):
        super().__init__(*args, **kwargs)
        route.register_router(self)

        self.config.from_object(config)
