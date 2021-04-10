from os import environ as env
from pyrogram import Client, filters

API_ID = env['API_ID']
API_HASH = env['API_HASH']
USERBOT_STRING_SESSION = env['USERBOT_STRING_SESSION']
CHANNEL = int(env['CHANNEL_ID'])

bot = Client(USERBOT_STRING_SESSION, API_ID, API_HASH)


@bot.on_message(filters.incoming & filters.channel & ~filters.chat(CHANNEL))
async def copy(bot, message):
    await message.copy(CHANNEL)


bot.run()
