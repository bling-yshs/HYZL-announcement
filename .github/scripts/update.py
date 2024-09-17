import json

# 读取用户输入的命令行参数
import sys
import time


def main():
    if len(sys.argv) < 2:
        return
    new_content = sys.argv[1]

    # 读取 announcement.json ，并解析成json格式
    with open('announcement.json', 'r', encoding='utf8') as f:
        buffer = f.read()
    # 这是一个数组，里面存放了多个公告
    announcement = json.loads(buffer)
    # 创建一个新的公告对象  {'version': 13, 'content': '签名爆了，等修吧，可能要几天，甚至再也回不来了...', 'timestamp': 1726388043, 'deprecated': True},
    new_announcement = {
        'version': announcement[0]['version'] + 1,
        'content': new_content,
        'timestamp': int(time.time()),
        'deprecated': False
    }
    # 将新的公告内容插入到 announcement 最前面
    announcement.insert(0, new_announcement)
    # 将新的 announcement 写入到 announcement.json 文件中
    with open('announcement.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(announcement, indent=2, ensure_ascii=False))


main()
