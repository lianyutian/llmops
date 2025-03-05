#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/5 14:42
@Author  : lianyutian
@File    : app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    query = StringField("query", validators=[
        DataRequired(message="query is required", ),
        Length(max=1000, message="query must be less than 1000 characters")
    ])
