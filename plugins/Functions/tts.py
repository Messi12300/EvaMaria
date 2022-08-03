from traceback import format_exc
from pyrogram import Client, filters
from asyncio import get_running_loop
from plugins.Lucifer import *

@Client.on_message(filters.command("tts"))
async def text_to_speech_en(_, message):
    if not message.reply_to_message:
        return await message.reply_text("**Reply To Same Text FFS**")
    if not message.reply_to_message.text:
        return await message.reply_text("**Reply To Same Text FFS**")
    m = await message.reply_text("__Processing...⏳️__")
    text = message.reply_to_message.text
    try:
        loop = get_running_loop()
        audio = await loop.run_in_executor(None, convert, text)
        await message.reply_audio(audio)
        await m.delete()
        audio.close()
    except Exception as e:
        await m.edit(e)
        e = format_exc()
        print(e)
