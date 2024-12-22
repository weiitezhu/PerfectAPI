# 使用官方的 Python 3.10 镜像作为基础镜像
FROM python

# 设置工作目录
WORKDIR /app

# 将本地的 requirements.txt 文件复制到容器中
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 将本地代码目录映射到容器中的 /app 目录
COPY . /app

# 容器启动时运行 FastAPI 应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
