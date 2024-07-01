import re


# 小驼峰转下划线
def camel_to_snake(text: str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

# 下划线转小驼峰
def snake_to_camel(text: str):
    words = text.split('_')
    return words[0] + ''.join(word.title() for word in words[1:])
