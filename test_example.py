"""示例代码 - 用于测试 AI Code Review"""

import os


def get_user_data(user_id):
    """获取用户数据"""
    # 问题1: SQL 注入风险
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return execute_query(query)


def divide(a, b):
    """除法运算"""
    # 问题2: 没有处理除零的情况
    return a / b


def read_config(filename):
    """读取配置文件"""
    # 问题3: 没有处理文件不存在的情况
    with open(filename) as f:
        return f.read()


def process_items(items):
    """处理列表"""
    # 问题4: 没有检查空列表
    first = items[0]
    return first.upper()


def save_password(password):
    """保存密码"""
    # 问题5: 明文存储密码
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")


API_KEY = "sk-1234567890abcdef"  # 问题6: 硬编码敏感信息
