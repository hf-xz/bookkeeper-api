# 记账工具-后端

使用 FastAPI + MongoDB

## 本地安装运行

1. 使用喜欢的方式创建虚拟环境

```sh
conda create -n fastapi python=3.12 -y
conda activate fastapi
```

2. 安装依赖

```sh
pip install fastapi pymongo
```

3. 配置环境变量

配置以下环境变量（配置到项目根目录的 `.env` 文件即可）

```text
MONGODB_URL=<connect_string>
MONGODB_DATABASE=<database_name>
```

4. 运行

```sh
python app.py
```
