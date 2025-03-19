#!/user/bin/.env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/4 15:06
@Author  : lianyutian
@File    : app_handler.py
"""
import os

from langchain.memory import ConversationBufferWindowMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI

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

        # 1.构建prompt&记忆
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant"),
            MessagesPlaceholder("chat_history"),
            ("human", "{query}")
        ])
        memory = ConversationBufferWindowMemory(k=3, input_key="query", return_messages=True,
                                                chat_memory=FileChatMessageHistory(
                                                    "../../storage/memory/chat_history.txt"))

        # 2. 构建大模型
        llm = ChatOpenAI(base_url=os.getenv("BASE_URL"))

        # 3. 构建解析器
        parser = StrOutputParser()

        # 3. 构建链
        chain = RunnablePassthrough.assign(
            chat_history=RunnableLambda(memory.load_memory_variables) | (
                lambda x: x.get("history"))) | prompt | llm | parser

        # 4. 调用链
        content = chain.invoke({"query": req.query.data})
        memory.save_context({"query": req.query.data}, {"output": content})

        return success_json({"content": content})

    def ping(self):
        """ping"""
        raise NotFoundException("数据未查询到")
