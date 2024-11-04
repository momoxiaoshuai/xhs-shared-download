#!/usr/bin/python3
# encoding:utf-8
from flask import Flask, send_from_directory, jsonify, request,make_response
import requests
import re
import json
from lxml import html
from flask_cors import CORS
api = Flask(__name__)
CORS(api)


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}


@api.route('/')
def index():
    return send_from_directory('static', 'index.html')


# 自定义api
@api.route('/api/images', methods=['POST'])
def img_download():
    share_url = request.json.get('shareUrl')
    if share_url:
      short_url = parse_share(share_url)
      html_content = requests.get(short_url,headers=headers).content
      tree = html.fromstring(html_content)
      title_link = tree.xpath('//*[@id="detail-title"]/text()')[0] 
      img_list = tree.xpath('//meta[@name="og:image"]/@content')  
      if title_link and img_list :
          data={}
          data['code']= 200
          data['message']=''
          data['data'] = img_list
          return json.dumps(data,ensure_ascii=False)  
      
@api.route('/proxy_image')
def proxy_image():
    image_url = request.args.get('url')
    if not image_url:
        return jsonify({'code': 400, 'message': '缺少图片 URL'}), 400

    response = requests.get(image_url)
    if response.status_code == 200:
        return (response.content, response.status_code, {'Content-Type': response.headers['Content-Type']})
    return jsonify({'code': response.status_code, 'message': '无法访问图片'}), response.status_code



@api.route('/api/download', methods=['GET'])
def download():
    try:
        img_url =  request.args.get('url')
        if not img_url:
            return "URL不能为空", 400
        response = requests.get(img_url, headers=headers)
        response.raise_for_status()
        # 创建响应
        resp = make_response(response.content)
        resp.headers['Content-Type'] = 'image/jpeg'  # 设置正确的内容类型
        resp.headers['Content-Disposition'] = 'attachment;filename=image.jpg'
        return resp
    except Exception as e:
        return f"下载失败: {str(e)}", 500


@api.route('/api/video',methods=['GET'])
def video_dowload():
  #from-data格式参数
  share_url = request.json.get('shareUrl')
  if share_url:
      short_url = parse_share(share_url)
      html_content = requests.get(short_url).content
      tree = html.fromstring(html_content)
      video_keywords =  tree.xpath('//meta[@name="keywords"]/@content')[0]
      video_link =  tree.xpath('//meta[@name="og:video"]/@content')[0]
      video_time = tree.xpath('//meta[@name="og:videotime"]/@content')[0]
      if video_link and video_keywords and video_time :
          data={}
          obj={'keyword':video_keywords,'link':video_link,'time':video_time}
          data['code']= 200
          data['message']=''
          data['data'] = obj
          return json.dumps(data,ensure_ascii=False)  


def parse_share(share_text):
    # 定义小红书短链接的正则表达式模式
    pattern = r'http://xhslink\.com/\S+'
    
    # 查找匹配的链接
    match = re.search(pattern, share_text)
    
    if match:
        short_url = match.group(0).split('，')[0].strip()
        return short_url
    return None


if __name__ == '__main__':
  api.run(port=10010,debug=True,host='0.0.0.0') # 启动服务
  # debug=True,改了代码后，不用重启，它会自动重启
  # 'host='127.0.0.1'别IP访问地址