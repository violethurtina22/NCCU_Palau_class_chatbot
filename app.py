from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('QjOVzhbNTmkJFuJSgyO+Vgl7ka8lDCJhP8+xNx5hEeOEHneia1Nt0S5R8QBHU/hLk6HsnuS2Ze/YHJE+Xp4p6yDZmNkObP1wmg4SkJRau/7hwf1MBEzMRI5e0wWBTaRGtO0ArG8pzvvO1R+U7r7iJgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b3aae31fbbf8b80f6342b0059dd2cb46')



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

    ### 這裡可以自行增加code
    message = TextSendMessage(text= "沒事幹嘛密我")
    line_bot_api.reply_message(event.reply_token, message)



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)