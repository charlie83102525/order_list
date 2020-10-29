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

a =[]
app = Flask(__name__)

line_bot_api = LineBotApi('4gsemJ/i1qNM87TDrM0VcZkIO8/UHCeq/3/mCtXb/EuUUdH7iwQtVY6WKrym9dn2sIoeVmMRZgM9gs2dQ0L5feeQUD/WxO6WXyWO5FKFtLhfQgBWDa0AEz1VFYwQhVzuQutykL29+yFA2Wiapu25ZwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0e4857dbcd8e9b8bf9f147b097df1937')



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
        a.append(r)

    else:
        r = '親，請輸入「+數量」'

    #global order_list
    #order_list = []
    #order_list.append(r)
    #order_list_df = pandas.DataFrame(order_list)
    #order_list_df.colume = ['orderifo']
    #with lite.connect('order_list.sqlite') as db:
        #order_list_df.to_sql('order_list', con = db)


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=','.join(a))


if __name__ == "__main__":
    app.run()