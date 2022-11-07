
#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================


def get_pic1():
    message = ImageSendMessage(
            original_content_url='https://i.pinimg.com/736x/af/90/19/af9019c179c33b4794da660099a0b14f.jpg',
            preview_image_url='https://i.pinimg.com/736x/af/90/19/af9019c179c33b4794da660099a0b14f.jpg'
        )
       
    return message

def get_pic2():
    message = TemplateSendMessage(
        alt_text='貓貓午安',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://img.cutenesscdn.com/630x/clsd/getty/66558346bedd4ccf97886e6eb24bc781.jpg?type=webp',
                    title='今天天氣如何?',
                    text='好想出去玩><',
                    actions=[
                        MessageTemplateAction(
                            label='大太陽',
                            text='大太陽'
                        ),
                        MessageTemplateAction(
                            label='陰天',
                            text='陰天'
                        ),
                        MessageTemplateAction(
                            label='雨天',
                            text='雨天'
                        ),
                    ]
                ),
                
            ]
        )
    )
    
    return message

def get_pic21():
    message = ImageSendMessage(
            original_content_url='https://media.istockphoto.com/photos/cat-sleeping-on-the-bed-picture-id821467204?k=20&m=821467204&s=612x612&w=0&h=x1cPN0Hx2KU39FLltWHg5s3AvkZCQ0fbP6BsbJk2eQA=',
            preview_image_url='https://media.istockphoto.com/photos/cat-sleeping-on-the-bed-picture-id821467204?k=20&m=821467204&s=612x612&w=0&h=x1cPN0Hx2KU39FLltWHg5s3AvkZCQ0fbP6BsbJk2eQA='
        )
        
    return message

def get_pic22():
    message = ImageSendMessage(
            original_content_url='https://c4.wallpaperflare.com/wallpaper/858/847/781/cat-yawn-stretch-hd-brown-tabby-kitten-wallpaper-thumb.jpg',
            preview_image_url='https://c4.wallpaperflare.com/wallpaper/858/847/781/cat-yawn-stretch-hd-brown-tabby-kitten-wallpaper-thumb.jpg'
        )
    
    return message

def get_pic23():
    message = ImageSendMessage(
            original_content_url='https://media.istockphoto.com/photos/cat-looking-out-on-a-rainy-day-picture-id1225813778?k=20&m=1225813778&s=612x612&w=0&h=S76CnlKpAXUUeckYcuHGKKxfKUst4pGzMTe_2lqpC3A=',
            preview_image_url='https://media.istockphoto.com/photos/cat-looking-out-on-a-rainy-day-picture-id1225813778?k=20&m=1225813778&s=612x612&w=0&h=S76CnlKpAXUUeckYcuHGKKxfKUst4pGzMTe_2lqpC3A='
        )
    return message

def get_pic3():
    message = ImageSendMessage(
            original_content_url='https://cdn.pixabay.com/photo/2019/05/08/21/21/cat-4189697__340.jpg',
            preview_image_url='https://cdn.pixabay.com/photo/2019/05/08/21/21/cat-4189697__340.jpg'
        )
    return message

def get_pic4():
    message = ImageSendMessage(
            original_content_url='https://i.imgur.com/WktFupP.jpeg',
            preview_image_url='https://i.imgur.com/WktFupP.jpeg'
        )
    return message

def get_pic5():
    message = ImageSendMessage(
            original_content_url='https://i.imgur.com/JOKsNeT.jpeg',
            preview_image_url='https://i.imgur.com/JOKsNeT.jpeg'
        )
    return message

def get_pic6():
    message = ImageSendMessage(
            original_content_url='https://i.imgur.com/rFBiyeR.jpeg',
            preview_image_url='https://i.imgur.com/rFBiyeR.jpeg'
        )
    return message