#!/user/bin/.env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/4 15:09
@Author  : lianyutian
@File    : router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """路由"""
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        # 创建蓝图
        bp = Blueprint('llmops', __name__, url_prefix="")

        # 将 url 与对应控制器方法做绑定
        bp.add_url_rule('/ping', view_func=self.app_handler.ping)
        bp.add_url_rule('/app/completion', methods=["POST"], view_func=self.app_handler.completion)

        # 注册蓝图
        app.register_blueprint(bp)
