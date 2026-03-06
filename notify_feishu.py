import requests
import json
import os

def send_to_feishu(content):
    # 从 GitHub Secrets 获取 Webhook URL，保护隐私
    url = os.environ.get("FEISHU_WEBHOOK_URL")
    
    # 构造飞书卡片消息（比纯文本更美观）
    payload = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "content": "📰 NewsNow 每日热点推送"}
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {"tag": "lark_md", "content": content}
                },
                {
                    "tag": "hr"
                },
                {
                    "tag": "note",
                    "elements": [{"tag": "plain_text", "content": "来自 GitHub Actions 自动化任务"}]
                }
            ]
        }
    }
    
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

# 在 NewsNow 抓取完数据后，筛选出你感兴趣的新闻条目并调用
# 示例：
# news_list = ["1. 某科技大事件 - [链接](url)", "2. 行业新动态 - [链接](url)"]
# send_to_feishu("\n".join(news_list))
