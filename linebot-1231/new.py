#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def test():
    message = TemplateSendMessage(
        alt_text='請接收狗狗的愛',
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

def dogtype():
    message = TemplateSendMessage(
        alt_text='請接收狗狗的愛',
        template=ImageCarouselTemplate(
            columns=
            [
                ImageCarouselColumn(
                    image_url="https://cdn2.ettoday.net/images/4703/4703917.jpg",
                    action=URITemplateAction(
                        label="柴犬",
                        uri="https://peipei1101.pixnet.net/blog/post/312944140"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://lh3.googleusercontent.com/proxy/GZIx7cvUO1nP8KhS_tTpS-k_UkBZkAHWO9VIk1HJ6NTsGTiUrfg06BOZikfvPUuRKKktxiEYmB9S04e50YgexScksBGABga4Dv4CHCR7gZYD5LsK",
                    action=URITemplateAction(
                        label="哈士奇",
                        uri="https://teachers.wyes.tn.edu.tw/students/no7/s90161/public_html/%E5%B0%88%E9%A1%8C%E7%B6%B2/%E5%93%88%E5%A3%AB%E5%A5%87%E7%9A%84%E7%B0%A1%E4%BB%8B.htm"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://www.hotpets.com.tw/wp-content/uploads/2017/03/%E8%A8%93%E7%B7%B4%E5%B8%AB%E7%9C%BC%E4%B8%AD%E7%9A%84%E7%B1%B3%E5%85%8B%E6%96%AF-%E5%B9%BC%E7%8A%AC.jpg",
                    action=URITemplateAction(
                        label="米克斯",
                        uri="https://www.petbacker.com.tw/blog/%E7%A4%BE%E5%8C%BA/%E7%88%B2%E4%BB%80%E9%BA%BD70-%E7%9A%84%E6%AD%90%E7%BE%8E%E4%BA%BA%E9%81%B8%E6%93%87%E9%A4%8Amix%EF%BC%88%E5%9C%9F%E7%8B%97%EF%BC%89%EF%BC%9F%E5%AE%83%E7%9A%84%E5%84%AA%E5%8B%A2%E4%BD%A0%E4%B8%8D%E6%87%82%EF%BC%81"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://images.chinatimes.com/newsphoto/2020-08-01/656/20200801001420.jpg",
                    action=URITemplateAction(
                        label="黃金獵犬",
                        uri="https://ea00336.pixnet.net/blog/post/46113198"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://images.twgreatdaily.com/images/elastic/M07/M07qbXIBd4Bm1__YXct2.jpg",
                    action=URITemplateAction(
                        label="馬爾濟斯",
                        uri="https://petonea.com/7887/"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://pic.pimg.tw/lapetrick/1420614632-2950473719_m.jpg",
                    action=URITemplateAction(
                        label="臘腸狗",
                        uri="https://kknews.cc/zh-tw/pet/oealbnm.html"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://img.ruten.com.tw/s2/2/c9/34/21733919759668_285.jpg",
                    action=URITemplateAction(
                        label="鬥牛犬",
                        uri="https://kknews.cc/zh-tw/pet/4xa8o2q.html"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://img.ruten.com.tw/s2/c/91/b2/21839710637490_181.jpg",
                    action=URITemplateAction(
                        label="巴哥犬",
                        uri="https://dogsbestlife.com.tw/foster-the-pugs/"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://images.chinatimes.com/newsphoto/2020-09-29/1024/20200929001326.jpg",
                    action=URITemplateAction(
                        label="博美犬",
                        uri="https://www.twgreatdaily.com/cat74/node456219"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://img.ltn.com.tw/Upload/news/600/2015/10/11/phplMDJ3m.jpg",
                    action=URITemplateAction(
                        label="米格魯",
                        uri="https://petbird.tw/article7216.html"
                    )
                )
            ]
        )
    )
    return message


def dogtalent():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://ipetgroup.com/photo/12973_0_620.jpeg",
                    action=URITemplateAction(
                        label="ㄅㄧㄤˋ",
                        uri="https://www.youtube.com/watch?v=28ZrJ8KeF_A&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=3"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://s2.best-wallpaper.net/wallpaper/1280x1024/1804/Dog-and-people-shake-hands_1280x1024.jpg",
                    action=URITemplateAction(
                        label="握手",
                        uri="https://www.youtube.com/watch?v=Hb5u_8tAL9k&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=5"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://www.wikihow.com/images_en/thumb/c/c3/Teach-Your-Dog-to-Sit-Step-13.jpg/v4-1200px-Teach-Your-Dog-to-Sit-Step-13.jpg",
                    action=URITemplateAction(
                        label="坐下",
                        uri="https://www.youtube.com/watch?v=8Y2ZCfxpWL0&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=12"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://www.pet321.com/uploadfile/2018/0409/a2a3acd0.jpg",
                    action=URITemplateAction(
                        label="趴下",
                        uri="https://www.youtube.com/watch?v=FcsOtp2kA2E&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=11"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.ytimg.com/vi/IX5GwKonJ_k/maxresdefault.jpg",
                    action=URITemplateAction(
                        label="狐蒙狗狗",
                        uri="https://www.youtube.com/watch?v=IX5GwKonJ_k&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=14"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://test.life.com.tw/data/news_3/38656/images/1499240d022cdcd673a17f7c11bf455e.jpg",
                    action=URITemplateAction(
                        label="拜託拜託",
                        uri="https://www.youtube.com/watch?v=Cn_Y0A5oCpw&list=PLOiMl5-7v0YU6_q-NPxFO8jdtm4nJS2gC&index=23"
                    )
                )
            ]
        )
    )
    return message