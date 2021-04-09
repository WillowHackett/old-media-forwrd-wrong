from pyrogram import Client, filters

API_ID = 'YOUR API ID'
API_HASH = 'YOUR API HASH'
USERBOT_STRING_SESSION = 'USERBOT STING SESSION'
CHANNEL = 'PRIVATE CHANNEL USERNAME OR ID'

bot = Client(USERBOT_STRING_SESSION, API_ID, API_HASH)


@bot.on_message(filters.incoming & filters.channel & ~filters.chat(CHANNEL))
async def forward(bot, message):
    await message.forward(CHANNEL)


bot.run()
