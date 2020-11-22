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
import pandas

import sqlite3 as lite

oo =[]
app = Flask(__name__)

line_bot_api = LineBotApi('')
handler = WebhookHandler('')



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


    profile = line_bot_api.get_profile(event.source.user_id)
    msg = event.message.text
 
    if msg[0] == '+':
        r = profile.display_name + '購買'+ msg[1:] + '份'
        oo.append(r)

    else:
        r = '親，請輸入「+數量」'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=',\n'.join(oo)))


if __name__ == "__main__":
    app.run()
