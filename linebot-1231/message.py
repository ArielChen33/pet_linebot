#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='最新的合作廠商有誰呢？',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #家樂福
                link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #生活市集
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #阿瘦皮鞋
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #塔吉特千層蛋糕
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #亞尼克生乳捲
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='請接收貓貓的愛',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/rUT9auY.png',
                    title='餵貓',
                    text='今天要餵什麼呢？',
                    actions=[
                        MessageTemplateAction(
                            label='營養飼料',
                            text='餵貓貓吃飼料'
                        ),
                        MessageTemplateAction(
                            label='罐罐',
                            text='餵食罐罐'
                        ),
                        URITemplateAction(
                            label='貓貓餵養須知',
                            uri='https://www.istoshare.com/intro/educationInfoItem/%E8%B2%93/3/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://cdn.hk01.com/di/media/images/1336545/org/d03892c053fad79121125c8586395fa9.jpg/s1uxEXdxiiVfI3cnXpezhJQqUWsJcm7W5AdOSeQHTkk?v=w1920',
                    title='清潔',
                    text='保持貓貓整潔很重要喲',
                    actions=[
                        MessageTemplateAction(
                            label='剪指甲',
                            text='今天不剪完指甲不許走>.<'
                        ),
                        MessageTemplateAction(
                            label='換貓砂',
                            text='好臭……但還是要換貓砂QQ'
                        ),
                        URITemplateAction(
                            label='貓貓清潔指南',
                            uri='https://catfirst.pixnet.net/blog/post/28145078'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.hiilan.com.tw/wp-content/uploads/2019/04/ExRevE1401621045547_6196_3.jpg',
                    title='運動',
                    text='要記得跟貓貓一起運動',
                    actions=[
                        MessageTemplateAction(
                            label='貓抓板',
                            text='貓抓板到貨了，來試試看'
                        ),
                        MessageTemplateAction(
                            label='逗貓棒',
                            text='玩啦，哪次不玩~'
                        ),
                         MessageTemplateAction(
                            label='貓草玩具',
                            text='咻咻咻————'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://image6.thenewslens.com/2020/9/rxmmtnksz4gossrgu7x12zyu012635.jpg?auto=compress&h=450&q=80&w=750',
                    title='我想成為貓貓爸媽',
                    text='陪伴永遠與責任共存',
                    actions=[
                        URITemplateAction(
                            label='我適合領養貓貓嗎？',
                            uri='https://stupidlove34.pixnet.net/blog/post/18779990'
                        ),
                        MessageTemplateAction(
                            label='找毛小孩',
                            text='我想要找周邊的合法寵物商店！'
                        ),
                        URITemplateAction(
                            label='請求協助',
                            uri='https://www.facebook.com/groups/349760251870471'
                        )
                    ]
                )
            ]
        )
    )
    return message

def dog1():
    message = TemplateSendMessage(
        alt_text='請接收狗狗的愛',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://pics.ettoday.net/images/2207/d2207536.jpg',
                    title='餵食',
                    text='成年狗一日約兩次---每個年紀不同',
                    actions=[
                        MessageTemplateAction(
                            label='狗狗可以吃',
                            text='狗狗可以吃的食物'
                        ),
                        MessageTemplateAction(
                            label='狗狗不能吃',
                            text='狗狗毒藥'
                        ),
                        URITemplateAction(
                            label='多久吃一次飯呢',
                            uri='https://udn.com/news/story/7470/5790888'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.ixintu.com/download/jpg/202001/322a94789a2d8b50c1e980b1b0127683.jpg!con',
                    title='清潔美容',
                    text='網美狗狗出沒',
                    actions=[
                        MessageTemplateAction(
                            label='洗澡',
                            text='狗狗洗澡'
                        ),
                        MessageTemplateAction(
                            label='剪指甲',
                            text='狗狗剪指甲'
                        ),
                        URITemplateAction(
                            label='狗狗日常清潔小撇步',
                            uri='https://kknews.cc/zh-tw/pet/o9bqq46.html'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i04piccdn.sogoucdn.com/39f924c8ab019c9d',
                    title='散步',
                    text='狗狗是你的減肥好夥伴呦~',
                    actions=[
                        MessageTemplateAction(
                            label='你的背包',
                            text='狗狗背包內容物'
                        ),
                        MessageTemplateAction(
                            label='散步時間到',
                            text='狗狗要散步'
                        ),
                        URITemplateAction(
                            label='狗狗每天要散步多久呢',
                            uri='https://running.biji.co/index.php?q=news&act=info&id=105413&subtitle=%E3%80%90%E6%AF%9B%E8%B5%B7%E4%BE%86%E3%80%91%E7%8B%97%E7%8B%97%E6%AF%8F%E6%97%A5%E6%95%A3%E6%AD%A5%E5%A4%9A%E4%B9%85%E6%89%8D%E5%90%88%E9%81%A9%EF%BC%9F5%20%E9%BB%9E%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A0%85%E4%B8%80%E6%AC%A1%E7%9C%8B%EF%BC%81'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ppfocus.com/2021/2/d6ed9c0ca4fa.jpg',
                    title='訓練',
                    text='只有懶主人沒有笨狗狗',
                    actions=[
                        URITemplateAction(
                            label='定時定點上廁所',
                            uri='https://www.pet100pa.com/about_pet/detail/%E7%8B%97%E4%BA%82%E5%B0%BF%E5%B0%BF'
                        ),
                        MessageTemplateAction(
                            label='狗狗基本技能',
                            text='狗狗基本技能'
                        ),
                        URITemplateAction(
                            label='訓練最佳時機',
                            uri='https://www.rocktail.com.tw/blog/view/70'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://lh3.googleusercontent.com/proxy/ab6Gi6xeRcs98JNmfyOkh20_ve88Xx0zBRsBYnuHCqKeVpe_vid4pmGJzNNfBFJJwOZ_PQnlGrd3DorWul-KWg8u72-0KpUh83VYBfM7y4pCv6hl5w',
                    title='玩耍',
                    text='不給糧就搗蛋，你給了我還是要搗蛋哈哈哈哈哈',
                    actions=[
                        MessageTemplateAction(
                            label='陪我接飛盤~',
                            text='把飛盤丟出去'
                        ),
                        MessageTemplateAction(
                            label='買玩具給我~',
                            text='狗狗常見玩具'
                        ),
                        URITemplateAction(
                            label='搗蛋鬼別搗蛋',
                            uri='https://kknews.cc/zh-tw/pet/javkkbq.html'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.chinatimes.com/newsphoto/2021-06-30/656/20210630003334.jpg',
                    title='我要成為狗爸媽',
                    text='終養不棄養',
                    actions=[
                        MessageTemplateAction(
                            label='你家寶貝的種族',
                            text='狗狗種類'
                        ),
                        MessageTemplateAction(
                            label='有認證的寵物店',
                            text='我想要找周邊的合法寵物商店！'
                        ),
                        URITemplateAction(
                            label='養前須知',
                            uri='https://imdognuts.com/keep-a-dog/'
                        )
                    ]
                )
            ]
        )
    )
    return message



############
# def dogtype():
#     message = TemplateSendMessage(
#         alt_text='圖片旋轉木馬',
#         template=ImageCarouselTemplate(
#             columns=
#             [
#                 ImageCarouselColumn(
#                     image_url="https://cdn2.ettoday.net/images/4703/4703917.jpg",
#                     action=URITemplateAction(
#                         label="柴犬",
#                         uri="https://peipei1101.pixnet.net/blog/post/312944140"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://lh3.googleusercontent.com/proxy/GZIx7cvUO1nP8KhS_tTpS-k_UkBZkAHWO9VIk1HJ6NTsGTiUrfg06BOZikfvPUuRKKktxiEYmB9S04e50YgexScksBGABga4Dv4CHCR7gZYD5LsK",
#                     action=URITemplateAction(
#                         label="哈士奇",
#                         uri="http://teachers.wyes.tn.edu.tw/students/no7/s90161/public_html/%E5%B0%88%E9%A1%8C%E7%B6%B2/%E5%93%88%E5%A3%AB%E5%A5%87%E7%9A%84%E7%B0%A1%E4%BB%8B.htm"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://www.hotpets.com.tw/wp-content/uploads/2017/03/%E8%A8%93%E7%B7%B4%E5%B8%AB%E7%9C%BC%E4%B8%AD%E7%9A%84%E7%B1%B3%E5%85%8B%E6%96%AF-%E5%B9%BC%E7%8A%AC.jpg",
#                     action=URITemplateAction(
#                         label="米克斯",
#                         uri="https://www.petbacker.com.tw/blog/%E7%A4%BE%E5%8C%BA/%E7%88%B2%E4%BB%80%E9%BA%BD70-%E7%9A%84%E6%AD%90%E7%BE%8E%E4%BA%BA%E9%81%B8%E6%93%87%E9%A4%8Amix%EF%BC%88%E5%9C%9F%E7%8B%97%EF%BC%89%EF%BC%9F%E5%AE%83%E7%9A%84%E5%84%AA%E5%8B%A2%E4%BD%A0%E4%B8%8D%E6%87%82%EF%BC%81"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://images.chinatimes.com/newsphoto/2020-08-01/656/20200801001420.jpg",
#                     action=URITemplateAction(
#                         label="黃金獵犬",
#                         uri="https://ea00336.pixnet.net/blog/post/46113198"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://images.twgreatdaily.com/images/elastic/M07/M07qbXIBd4Bm1__YXct2.jpg",
#                     action=URITemplateAction(
#                         label="馬爾濟斯",
#                         uri="https://petonea.com/7887/"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="http://pic.pimg.tw/lapetrick/1420614632-2950473719_m.jpg",
#                     action=URITemplateAction(
#                         label="臘腸狗",
#                         uri="https://kknews.cc/zh-tw/pet/oealbnm.html"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://img.ruten.com.tw/s2/2/c9/34/21733919759668_285.jpg",
#                     action=URITemplateAction(
#                         label="鬥牛犬",
#                         uri="https://kknews.cc/zh-tw/pet/4xa8o2q.html"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://img.ruten.com.tw/s2/c/91/b2/21839710637490_181.jpg",
#                     action=URITemplateAction(
#                         label="巴哥犬",
#                         uri="https://dogsbestlife.com.tw/foster-the-pugs/"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://images.chinatimes.com/newsphoto/2020-09-29/1024/20200929001326.jpg",
#                     action=URITemplateAction(
#                         label="博美犬",
#                         uri="https://www.twgreatdaily.com/cat74/node456219"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://img.ltn.com.tw/Upload/news/600/2015/10/11/phplMDJ3m.jpg",
#                     action=URITemplateAction(
#                         label="米格魯",
#                         uri="https://petbird.tw/article7216.html"
#                     )
#                 )
#             ]
#         )
#     )
#     return message

########
# def dogtalent():
#     message = TemplateSendMessage(
#         alt_text='圖片旋轉木馬',
#         template=ImageCarouselTemplate(
#             columns=[
#                 ImageCarouselColumn(
#                     image_url="https://ipetgroup.com/photo/12973_0_620.jpeg",
#                     action=URITemplateAction(
#                         label="ㄅㄧㄤˋ",
#                         uri="https://www.youtube.com/watch?v=28ZrJ8KeF_A&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=3"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://s2.best-wallpaper.net/wallpaper/1280x1024/1804/Dog-and-people-shake-hands_1280x1024.jpg",
#                     action=URITemplateAction(
#                         label="握手",
#                         uri="https://www.youtube.com/watch?v=Hb5u_8tAL9k&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=5"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://www.wikihow.com/images_en/thumb/c/c3/Teach-Your-Dog-to-Sit-Step-13.jpg/v4-1200px-Teach-Your-Dog-to-Sit-Step-13.jpg",
#                     action=URITemplateAction(
#                         label="坐下",
#                         uri="https://www.youtube.com/watch?v=8Y2ZCfxpWL0&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=12"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://www.pet321.com/uploadfile/2018/0409/a2a3acd0.jpg",
#                     action=URITemplateAction(
#                         label="趴下",
#                         uri="https://www.youtube.com/watch?v=FcsOtp2kA2E&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=11"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="https://i.ytimg.com/vi/IX5GwKonJ_k/maxresdefault.jpg",
#                     action=URITemplateAction(
#                         label="狐蒙狗狗",
#                         uri="https://www.youtube.com/watch?v=IX5GwKonJ_k&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=14"
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url="http://test.life.com.tw/data/news_3/38656/images/1499240d022cdcd673a17f7c11bf455e.jpg",
#                     action=URITemplateAction(
#                         label="拜託拜託",
#                         uri="https://www.youtube.com/watch?v=Cn_Y0A5oCpw&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=23"
#                     )
#                 )
#             ]
#         )
#     )
#     return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例