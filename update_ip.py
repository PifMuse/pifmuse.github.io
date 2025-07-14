import requests
from datetime import datetime
import os

def get_public_ip():
    try:
        response = requests.get("https://ifconfig.me/ip", timeout=5)
        return response.json()["ip"]
    except Exception as e:
        print(f"获取IP失败: {e}")
        return None

def update_html(ip):
    # 读取现有HTML内容
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    
    # 替换IP和更新时间
    updated_content = content.replace(
        '<div id="ip">加载中...</div>',
        f'<div id="ip">{ip}</div>'
    ).replace(
        '<span id="time"></span>',
        f'<span id="time">{datetime.now()}</span>'
    )
    
    # 写回文件
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    ip = get_public_ip()
    if ip:
        update_html(ip)
        print(f"IP已更新到网页: {ip}")
    else:
        print("无法更新IP")
