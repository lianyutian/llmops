#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/7 15:46
@Author  : lianyutian
@File    : conftest.py
"""
import pytest

from app.http.app import app


@pytest.fixture
def client():
    """获取Flask应用测试client"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
