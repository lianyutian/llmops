#!/user/bin/.env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/4 16:17
@Author  : lianyutian
@File    : app.py
"""
import dotenv
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import Http

# 将.env加载到环境变量中
dotenv.load_dotenv()
injector = Injector()
config = Config()
app = Http(__name__, config=config, route=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
