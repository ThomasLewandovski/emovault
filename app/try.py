import sys
import os
# 添加项目根目录到路径，以便 Python 能找到相关模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.dialogue_model import DeepSeekDialogueGenerator
from app.sentiment_analysis import sentiment_analyzer

# 从环境变量获取API密钥
import os
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("警告：未设置DEEPSEEK_API_KEY环境变量，请设置后再运行")
    exit(1)

# 初始化对话生成器
dialogue_generator = DeepSeekDialogueGenerator(api_key)

while True:
    user_input = input("请输入你的话语（输入 '退出' 结束对话）: ")
    if user_input.lower() == '退出':
        break

    # 进行情感分析
    sentiment_result = sentiment_analyzer([user_input])[0]
    sentiment_label = sentiment_result['label']
    sentiment_score = sentiment_result['score']
    print(f"你输入内容的情感标签是: {sentiment_label}，置信度: {sentiment_score:.4f}")

    # 根据情感标签修改提示
    if sentiment_label == 'POSITIVE':
        prompt = f"用户输入了积极的内容：{user_input}，请给出积极回应。"
    elif sentiment_label == 'NEGATIVE':
        prompt = f"用户输入了消极的内容：{user_input}，请安慰用户。"
    else:
        prompt = user_input

    try:
        # 生成对话
        response = dialogue_generator.generate(prompt)
        print("回复内容: ", response)
    except Exception as e:
        print(f"生成对话时出错: {e}")