import json
import os
from sentence_transformers import (SentenceTransformer, util)

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 知识库文件的路径
knowledge_base_path = os.path.join(current_dir, '../data/knowledge_base.json')

# 加载知识库
with open(knowledge_base_path, 'r', encoding='utf-8') as f:
    knowledge_base = json.load(f)

# 加载嵌入模型
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 为知识库中的每条建议计算嵌入
for entry in knowledge_base:
    entry['embedding'] = model.encode(entry['emotion'], convert_to_tensor=True)


def get_best_advice(user_text):
    """
    根据用户输入，检索最相关的建议。
    :param user_text: 用户输入的文本
    :return: 最匹配的建议字符串
    """
    user_embedding = model.encode(user_text, convert_to_tensor=True)

    best_match = None
    best_score = 0

    for entry in knowledge_base:
        similarity = util.pytorch_cos_sim(user_embedding, entry['embedding']).item()

        if similarity > best_score:
            best_score = similarity
            best_match = entry

    return best_match['advice'] if best_match else "目前没有合适的建议，但请相信你会找到方向！"