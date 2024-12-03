# 使用官方的Python基础镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 将当前目录中的内容复制到容器中的 /app 目录
COPY . /app

# 安装项目的依赖（假设你的依赖列在 requirements.txt 中）
RUN pip install --no-cache-dir -r requirements.txt

# 暴露容器的端口
EXPOSE 10010

# 设置环境变量，确保 Flask 启动时不会以调试模式运行
ENV FLASK_APP=app.py

# 启动 Flask 服务
CMD ["python", "app.py"]
