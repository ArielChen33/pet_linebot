from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

# import threading 

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from newmap import *
from pic import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time

from pic import get_pic1, get_pic2, get_pic21, get_pic22, get_pic23, get_pic3, get_pic4, get_pic5
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('rZS6SrOpjJp+uv3oETBXr6Kbkg+wOpbH3dvnIR2eroRqnMKFUBrvn5c2OWY0RobIetijH29itu+X9zdn4CaHe5JVzWqRBbkZ6PqU1OUcm6j4YcXQmadDGgfmorDQbcbBeeSJi2/cskhqSZ7lwPi7TwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7ef36f32bfedab099ee3ba2a021443b6')

# import schedule  
# import time  

# uid = 'Ud6a80788a301a6bc9d75dd9a2dd4eef4'
#     def job() :
#         message = TextSendMessage(text='給我去遛狗')
#         line_bot_api.push_message(uid,message)
#         #for i in range(0:1:7):

# schedule.every().day.at('02:03').do(job)

#def push_message():  
 #    message = TextSendMessage(text='你好啊你好')
  #      line_bot_api.push_message(uid,message)

#def push_message():
#    while datetime.datetime()==datetime(2021,12,30,01,13,30):
        #time.sleep(20)
       

#threading.Thread(target=push_message).start()
    
    
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = text = event.message.text
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    if '我想要獲取其他關鍵字！' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/vtHsBLU.jpg',
            preview_image_url='https://i.imgur.com/vtHsBLU.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    if '我想要找周邊的合法寵物商店！' in msg:
        message = TextSendMessage(text = '請傳送你的位置')
        line_bot_api.reply_message(event.reply_token, message)
    if '餵貓貓吃飼料' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/glZgerG.png',
            preview_image_url='https://i.imgur.com/glZgerG.png'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    if '餵食罐罐' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/HrztVv8.png',
            preview_image_url='https://i.imgur.com/HrztVv8.png'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    if '今天不剪完指甲不許走>.<' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://mewcare.com/wp-content/uploads/2019/12/cat-cut-nail.jpg',
            preview_image_url='https://mewcare.com/wp-content/uploads/2019/12/cat-cut-nail.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    if '好臭……但還是要換貓砂QQ' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://leedecat.com/wp-content/uploads/2020/06/102.jpg',
            preview_image_url='https://leedecat.com/wp-content/uploads/2020/06/102.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    if '貓抓板到貨了，來試試看' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/yW1PbgS.png',
            preview_image_url='https://i.imgur.com/yW1PbgS.png'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    if '玩啦，哪次不玩~' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/cH1aRmC.png',
            preview_image_url='https://i.imgur.com/cH1aRmC.png'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    if '咻咻咻————' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/dIZwiGV.png',
            preview_image_url='https://i.imgur.com/dIZwiGV.png'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    if '狗狗基本技能' in msg:
        message = dogtalent()
        line_bot_api.reply_message(event.reply_token, message)
    if '狗狗任務選單' in msg:
        message = dog1()
        line_bot_api.reply_message(event.reply_token, message)
    if '狗狗種類' in msg:
        message = dogtype()
        line_bot_api.reply_message(event.reply_token, message)
    if '狗狗可以吃的食物' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i2.kknews.cc/Eq5qQ9Fe4C_rAq4qqls2Eed2Q9mOWn7V1JFDNdQ/0.jpg',
            preview_image_url='https://i2.kknews.cc/Eq5qQ9Fe4C_rAq4qqls2Eed2Q9mOWn7V1JFDNdQ/0.jpg')
        line_bot_api.reply_message(event.reply_token, image_message)
    if '狗狗毒藥' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i1.kknews.cc/KyDXEML4mjANKuCC-H8o14WPnKhFrBREBFxNa1c/0.jpg',
            preview_image_url='https://i1.kknews.cc/KyDXEML4mjANKuCC-H8o14WPnKhFrBREBFxNa1c/0.jpg')
        line_bot_api.reply_message(event.reply_token, image_message)
    if '狗狗洗澡' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://maoup.com.tw/wp-content/uploads/2015/08/150827_11.png',
            preview_image_url='https://maoup.com.tw/wp-content/uploads/2015/08/150827_11.png')
        line_bot_api.reply_message(event.reply_token, image_message)
    if '狗狗背包內容物' in msg :
        image_message = ImageSendMessage(
            original_content_url='https://maoup.com.tw/wp-content/uploads/2018/05/170903_12.png',
            preview_image_url='https://maoup.com.tw/wp-content/uploads/2018/05/170903_12.png')
        line_bot_api.reply_message(event.reply_token, image_message)
    if '狗狗要散步' in msg :
        image_message = ImageSendMessage(
            original_content_url='https://maoup.com.tw/wp-content/uploads/2016/10/1610111.png',
            preview_image_url='https://maoup.com.tw/wp-content/uploads/2016/10/1610111.png')
        line_bot_api.reply_message(event.reply_token, image_message)
    if '把飛盤丟出去' in msg :
        image_message = ImageSendMessage(
            original_content_url='https://www.chongso.com/uploads/allimg/191101/3-191101095600.jpg',
            preview_image_url='https://www.chongso.com/uploads/allimg/191101/3-191101095600.jpg')
        line_bot_api.reply_message(event.reply_token, image_message)
    if '狗狗常見玩具' in msg :
        image_message = ImageSendMessage(
            original_content_url='https://maoup.com.tw/wp-content/uploads/2015/09/150831_11.png',
            preview_image_url='https://maoup.com.tw/wp-content/uploads/2015/09/150831_11.png')
        line_bot_api.reply_message(event.reply_token, image_message)
    if '狗狗剪指甲' in msg :
        image_message = ImageSendMessage(
            original_content_url='https://7627.cyberbiz.tw/s/files/7627/ckeditor/pictures/content_8ec1e5dc-1d9e-4a48-9dd0-c5416a8f5b35.jpg',
            preview_image_url='https://7627.cyberbiz.tw/s/files/7627/ckeditor/pictures/content_8ec1e5dc-1d9e-4a48-9dd0-c5416a8f5b35.jpg')
        line_bot_api.reply_message(event.reply_token, image_message)
    # if 'hi' in msg:
    #      line_bot_api.reply_message(  # 回復傳入的訊息文字
    #          event.reply_token,
    #          TemplateSendMessage(
    #             alt_text='Buttons template',
    #             template=ButtonsTemplate(
    #                 title='Menu',
    #                 text='請選擇地區',
    #                 actions=[
    #                     MessageTemplateAction(
    #                         label='台北市',
    #                         text='台北市'
    #                     ),
    #                     MessageTemplateAction(
    #                         label='台中市',
    #                         text='台中市'
    #                     ),
    #                     MessageTemplateAction(
    #                         label='高雄市',
    #                         text='高雄市'
    #                     )
    #                 ]
    #             )
    #         )
    #     )
    if '貓貓任務選單' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    if '狗勾早安' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://tw.sunnypethouse.com/wp-content/uploads/2020/11/image-500x313.png',
            preview_image_url='https://tw.sunnypethouse.com/wp-content/uploads/2020/11/image-500x313.png'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    
    elif '狗勾午安' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/pOnQRyg.jpg',
            preview_image_url='https://i.imgur.com/pOnQRyg.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    
    elif '狗勾晚安' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/JgJwZYh.png',
            preview_image_url='https://i.imgur.com/JgJwZYh.png'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    
    elif '又亂咬欸你' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/XEv02Sx.jpg',
            preview_image_url='https://i.imgur.com/XEv02Sx.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    
    elif '吼你又亂大便' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/gdnSx4I.png',
            preview_image_url='https://i.imgur.com/gdnSx4I.png'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    
    elif '打我啊笨蛋' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/rFBiyeR.jpeg',
            preview_image_url='https://i.imgur.com/rFBiyeR.jpeg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    elif '喵喵早安' in msg:
        message = get_pic1()
        line_bot_api.reply_message(event.reply_token, message)
    elif '喵喵午安' in msg:
        message = get_pic2()
        line_bot_api.reply_message(event.reply_token, message)
    elif '大太陽' in msg:
        message = get_pic21()
        line_bot_api.reply_message(event.reply_token, message)
    elif '陰天' in msg:
        message = get_pic22()
        line_bot_api.reply_message(event.reply_token, message)
    elif '雨天' in msg:
        message = get_pic23()
        line_bot_api.reply_message(event.reply_token, message)
    elif '喵喵晚安' in msg:
        message = get_pic3()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我好無聊' in msg:
        message = get_pic4()
        line_bot_api.reply_message(event.reply_token, message)
    elif '工作中' in msg:
        message = get_pic5()
        line_bot_api.reply_message(event.reply_token, message)
    elif '打我啊笨蛋' in msg:
        message = get_pic6()
        line_bot_api.reply_message(event.reply_token, message)

    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)

@handler.add(MessageEvent)
def handle_message(event):
    if event.message.type == 'location':
        latitude = event.message.latitude
        longitude = event.message.longitude
        message = get_shop(latitude,longitude)
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
