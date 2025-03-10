import requests

class DeepSeekDialogueGenerator:
    def __init__(self, api_key, api_url="https://api.deepseek.com/v1/chat/completions"):
        """
        初始化 DeepSeek-R1 对话生成器。
        :param api_key: DeepSeek-R1 的 API 密钥
        :param api_url: DeepSeek-R1 的 API 地址
        """
        self.api_key = api_key
        self.api_url = api_url

    def generate(self, prompt, max_tokens=500, temperature=0.7):
        """
        调用 DeepSeek-R1 API 生成对话。
        :param prompt: 用户输入的提示文本
        :param max_tokens: 生成文本的最大长度
        :param temperature: 控制生成文本的随机性
        :return: 生成的对话文本
        """
        # 构造请求头
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # 构造请求体
        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        # 发送请求
        response = requests.post(self.api_url, headers=headers, json=data)

        # 检查响应状态
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            # 补充完整错误处理
            raise Exception(f"API 请求失败，状态码：{response.status_code}, 错误信息：{response.text}")


if __name__ == "__main__":
    # 从环境变量获取API密钥
    import os
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("警告：未设置DEEPSEEK_API_KEY环境变量，请设置后再运行")
        exit(1)
        
    # 初始化对话生成器
    dialogue_generator = DeepSeekDialogueGenerator(api_key)

    # 用户输入
    user_input = "我今天心情不好，因为工作压力很大。"

    # 生成对话
    try:
        generated_text = dialogue_generator.generate(user_input, max_tokens=100, temperature=0.7)
        print("用户输入：", user_input)
        print("生成的对话：", generated_text)
    except Exception as e:
        print("生成对话失败：", str(e))
