#!/user/bin/.env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/5 13:21
@Author  : lianyutian
@File    : example.py
"""

from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programing."
        }
    ]
)

print(completion.choices[0].message)
