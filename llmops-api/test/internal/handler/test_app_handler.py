#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/7 15:52
@Author  : lianyutian
@File    : test_app_handler.py.py
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:
    """app控制器测试类"""

    @pytest.mark.parametrize("query", [None, "你是谁"])
    def test_completion(self, query, client):
        response = client.post("/app/completion", json={"query": query})
        assert response.status_code == 200
        if query is None:
            assert response.json.get("code") == HttpCode.VALIDATION_ERROR
        else:
            assert response.json.get("code") == HttpCode.SUCCESS
