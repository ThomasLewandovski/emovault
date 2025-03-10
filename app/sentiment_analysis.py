from transformers import pipeline

# 加载多情绪分析模型（支持7种情绪：愤怒、厌恶、恐惧、快乐、中立、悲伤、惊讶）
sentiment_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)


def analyze_sentiment(text):
    """
    对用户输入的文本进行多情绪分析，并返回情绪占比。
    :param text: 用户输入的文本
    :return: 各个情绪类别的分数（如 {'joy': 88.5, 'sadness': 20.3}）
    """
    results = sentiment_analyzer(text)[0]  # 获取分析结果
    emotion_scores = {res['label']: round(res['score'] * 100, 2) for res in results}

    # 按情绪置信度排序（从高到低）
    sorted_emotions = dict(sorted(emotion_scores.items(), key=lambda item: item[1], reverse=True))

    return sorted_emotions


# 示例测试
if __name__ == "__main__":
    text = "I feel so sad and alone today."
    print(analyze_sentiment(text))