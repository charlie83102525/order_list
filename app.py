from flask import Flask, request, abort #用flask架設伺服器


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)


app = Flask(__name__)

line_bot_api = LineBotApi('pd+ozecWVTmcbqNeKmPNFf5JtkkhmJo4ELm2NT7d+0kR0nHDLndzIhp0H6Xh2/19TZCNdEydWH0rNOstXXv6+nuqa1g8OByP6EmGVbLYGsD3GC1Sus36DRfh1agyjZy5reufPMown4Cqiv/YBU9PRQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('72819c8cc7cd0b793af5431e5e632320')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #get user id when reply
    user_id = event.source.user_id
    print('user_id = ', user_id)
    msg = event.message.text
    r = '我看不懂你說什麼'
 

    order_list = []
    if msg == '+1':
        r = user_id, '購買1份'
        order_list.append(r)

    for ol in order_list:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=ol))


if __name__ == "__main__":
    app.run()