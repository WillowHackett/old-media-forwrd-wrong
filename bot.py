from pyrogram import Client, filters

API_ID = '3572022'
API_HASH = 'ca6eeadd66630f693f9289e6255c0bc6'
USERBOT_STRING_SESSION = 'AQCWdnmZShJyOjoJ1m2WbnQZzwPc5PzMYkG9IApGRVJnirCO0EoNAXu5mNg96XqK77dGXBEX4rlMWH86ujheuhJ6CWd23hZUQIh2_pw0xTSl0gTiWESDtCeTAbqvzE__XMzlP9hLVnfccwN_f2JuvZQBOMlKC0U7cxSO-0y4Oemw3KAZDbhTLYkOcCwjHPTSz1z7DN1FhKmqfgdzvq2XIi76w9haFmz9s5QT6wdnoPpaekxh6vc-Imuhyi157fq7Xa-tMqKBjrsH08aQWswCg9rUAZapCAFLKmyR_H3u0bYKcQ3GQMDIQ_dA5EGLrjiOzDQr9yHK9wJK9XQMAIlFGJ69Xdh14AA'
CHANNEL = '-1001439100729'

bot = Client(USERBOT_STRING_SESSION, API_ID, API_HASH)


@bot.on_message(filters.incoming & filters.channel & ~filters.chat(CHANNEL))
async def forward(bot, message):
    await message.forward(CHANNEL)


bot.run()
