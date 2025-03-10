import json

# 定义要保存到JSON文件的数据
data = [
    {
        "emotion": "焦虑",
        "advice": "当你感到焦虑时，尝试深呼吸，并专注于手头的任务，而不是未来的不确定性。"
    },
    {
        "emotion": "孤独",
        "advice": "加入学校社团，或者主动联系老朋友，增加社交互动。"
    },
    {
        "emotion": "迷茫",
        "advice": "制定一个小目标，比如每天学习 30 分钟，逐步寻找方向。"
    },
    {
        "emotion": "自卑",
        "advice": "列出自己的优点，每天阅读，增强自信心。"
    },
    {
        "emotion": "压力",
        "advice": "尝试时间管理技巧，将大任务分解为小步骤，逐一完成。"
    },
    {
        "emotion": "愤怒",
        "advice": "在表达愤怒前，先深呼吸，数到十，冷静下来再处理问题。"
    },
    {
        "emotion": "沮丧",
        "advice": "与信任的朋友或导师谈谈，倾诉你的感受，寻求支持。"
    }
]

# 定义JSON文件的路径
file_path = "/Users/mxx/Desktop/hugging_face/data/knowledge_base.json"

# 将数据保存到JSON文件
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON文件已生成：{file_path}")