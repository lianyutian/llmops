#!/user/bin/.env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/4 15:06
@Author  : lianyutian
@File    : app_handler.py
"""
import os

from openai import OpenAI

from internal.exception.exception import NotFoundException
from internal.schema.app_schema import CompletionReq
from pkg.response.response import success_json, validate_error_json


class AppHandler:
    """应用控制器"""

    def completion(self):
        """聊天接口"""
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2. 构建 OpenAi 的请求参数,并发起请求
        client = OpenAI(
            base_url=os.getenv("BASE_URL")
        )
        # 3. 返回结果
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {
                    "role": "user",
                    "content": req.query.data
                }
            ]
        )
        content = completion.choices[0].message.content

        return success_json({"content": content})

    def ping(self):
        """ping"""
        raise NotFoundException("数据未查询到")
