# 小红书图片下载工具

一个简单易用的小红书图片批量下载工具，支持去水印，适配移动端和桌面端。

## 功能特点

- 📱 完美适配移动端和桌面端
- 🚀 简单易用，粘贴分享文本即可使用
- 💫 支持长按（移动端）/ 右键（桌面端）保存图片

## 在线体验

访问地址：[xhs.wus.homes](https://xhs.wus.homes/)

## 使用说明

1. 打开小红书APP，点击分享按钮
2. 选择"复制链接"
3. 将复制的内容粘贴到输入框
4. 点击获取图片
5. 长按(手机)或右键(电脑)保存图片

## 部署说明

### Docker 部署（推荐）

克隆项目
git clone https://github.com/momoxiaoshuai/xhs-shared-download.git

进入项目目录
cd xiaohongshu-downloader

启动服务
docker compose up -d

默认端口：10010，如需修改请编辑 docker-compose.yml 文件

### 手动部署

1. 确保已安装 Python 3.7+
2. 安装依赖：`pip install -r requirements.txt`
3. 运行服务：`python main.py`

## 项目截图

![移动端效果](https://github.com/user-attachments/assets/6efc5a4c-a65b-40ec-8d7f-110e53d2cd2f)

![桌面端效果](https://github.com/user-attachments/assets/984e0731-e140-4d9b-a317-16c13841b497)

## 技术栈

- 前端：HTML5 + CSS3 + JavaScript
- 后端：Python
- 部署：Docker

## 注意事项

- 本工具仅供学习交流使用
- 请勿用于商业用途
