# 使用官方 Python 基礎映像
FROM python:3.10

# 設定工作目錄
WORKDIR /app

# 複製當前目錄內容到工作目錄中
COPY . /app

# 更新 pip 並安裝 Flask 及其他需求的套件
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 設定環境變數
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# 開放 Flask 的預設埠
EXPOSE 5000

# 執行 Flask 應用程式
CMD ["flask", "run"]
