EmoVault - 情绪分析聊天应用

项目介绍

EmoVault是一个基于人工智能的情绪分析聊天应用，能够分析用户输入的文本情绪，并根据情绪提供个性化的回应和建议。应用使用了情感分析模型和大语言模型，为用户提供情绪支持和交流平台。

主要功能

- 多情绪分析：使用情感分析模型识别用户文本中的7种情绪（愤怒、厌恶、恐惧、快乐、中立、悲伤、惊讶）
- 智能对话：基于DeepSeek API生成个性化回复
- 情绪建议：根据识别的情绪提供针对性建议
- 语音输入：支持语音识别，方便用户表达
- 聊天历史：保存对话记录，方便回顾

技术栈

- Python 3.8+
- Streamlit：Web界面框架
- Transformers：情感分析模型
- DeepSeek API：对话生成
- SpeechRecognition：语音识别
- Sentence-Transformers：文本嵌入和相似度计算

安装步骤

1. 克隆仓库
```bash
git clone https://github.com/ThomasLewandovski/emovault.git
cd emovault
```


2. 安装依赖
```bash
pip install -r requirements.txt
```


3. 设置环境变量

   方法一：使用.env文件（推荐）
   - 复制项目根目录中的`.env.example`文件并重命名为`.env`
   - 在`.env`文件中设置您的API密钥：

   DEEPSEEK_API_KEY=your_api_key_here

   
   方法二：直接设置系统环境变量
   ```bash
   # Linux/Mac
   export DEEPSEEK_API_KEY="your_api_key_here"  
   
   # Windows
   set DEEPSEEK_API_KEY=your_api_key_here
   ```
   

使用方法

1. 运行应用

   方法一：使用run_app.py脚本（推荐）
   ```bash
   python run_app.py
   ```
   
   方法二：直接使用streamlit
   ```bash
   streamlit run app/main.py
   ```

2. 在浏览器中访问应用（默认地址：http://localhost:8501）

3. 在聊天框中输入文字或使用语音输入功能

项目结构

```
.
├── app/                    # 应用主目录
│   ├── __init__.py
│   ├── dialogue_model.py   # 对话生成模型
│   ├── knowledge_base.py   # 知识库和建议检索
│   ├── main.py            # Streamlit应用主文件
│   ├── sentiment_analysis.py # 情感分析模型
│   └── SpeechRecognition.py # 语音识别功能
├── data/                   # 数据文件
│   └── knowledge_base.json # 情绪建议知识库
├── requirements.txt        # 项目依赖
└── run_app.py             # 应用启动脚本
```

注意事项

- 需要DeepSeek API密钥才能使用对话生成功能
- 首次运行时会下载情感分析模型，需要稳定的网络连接
- 语音识别功能需要麦克风权限

许可证

MIT