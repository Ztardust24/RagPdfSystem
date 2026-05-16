# -*- encoding: utf-8 -*-
"""
@File    : test_embedding.py.py
@Time    : 2026/4/21 17:28
@Version : v1.0
@Author  : Hui Zhang
@Contact : starrydrifter@163.com
@Software: PyCharm
@Description:
"""

import os
from dotenv import load_dotenv
load_dotenv()
from src.embedding.dashscope_embedding import DashScopeEmbeddingService

embedder = DashScopeEmbeddingService()
vectors = embedder.embed_documents(["测试文本"])
print("向量维度:", len(vectors[0]))


# dfg = os.getenv("DASHSCOPE_API_KEY")
#
# dda = os.getenv("DASHSCOPE_API_KEY")
# print(os.getenv("DASHSCOPE_API_KEY"))