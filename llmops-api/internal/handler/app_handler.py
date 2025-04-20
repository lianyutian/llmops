#!/user/bin/.env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/4 15:06
@Author  : lianyutian
@File    : app_handler.py
"""
import os
from typing import Dict, Any

from langchain.memory import ConversationBufferWindowMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.memory import BaseMemory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableConfig
from langchain_core.tracers import Run
from langchain_openai import ChatOpenAI

from internal.exception.exception import NotFoundException
from internal.schema.app_schema import CompletionReq
from pkg.response.response import success_json, validate_error_json


class AppHandler:
    """应用控制器"""

    @classmethod
    def _load_memory_variables(cls, input: Dict[str, Any], config: RunnableConfig):
        """加载记忆变量"""
        configurable = config.get("configurable")
        configurable_memory = configurable.get("memory", None)
        if configurable_memory is not None and isinstance(configurable_memory, BaseMemory):
            return configurable_memory.load_memory_variables(input)
        return {"history": []}

    @classmethod
    def _save_context(cls, run: Run, config: RunnableConfig) -> None:
        configurable = config.get("configurable", {})
        configurable_memory = configurable.get("memory", None)
        if configurable_memory is not None and isinstance(configurable_memory, BaseMemory):
            configurable_memory.save_context(run.inputs, run.outputs)

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
                                                    "D:\work\workspace\llmops\llmops-api\storage\memory\chat_history.txt"))

        # 2. 构建大模型
        llm = ChatOpenAI(base_url=os.getenv("BASE_URL"))

        # 3. 构建解析器
        parser = StrOutputParser()

        # 4. 构建链
        chain = (RunnablePassthrough.assign(
            chat_history=RunnableLambda(self._load_memory_variables) | (
                lambda x: x.get("history"))) | prompt | llm | parser).with_listeners(on_end=self._save_context)

        # 5. 调用链
        content = chain.invoke({"query": req.query.data}, config={"configurable": {"memory": memory}})

        return success_json({"content": content})

    def ping(self):
        """ping"""
        raise NotFoundException("数据未查询到")
