from pyrogram import Client, filters
from plugins import emoji

@Client.on_message(filters.command(["throw", "dart"]))
async def throw_dart(bot, update):
    replyID = query.from_user.id
    if update.reply_to_message:
        replyID = update.reply_to_message.id
    await bot.send_dice(chat_id=update.chat.id, emoji=emoji.THROW_DART, disable_notification=True, reply_to_message_id=replyID)

@Client.on_message(filters.command(["goal", "shoot"]))
async def roll_dice(bot, update):
    replyID = query.from_user.id
    if update.reply_to_message:
        replyID = update.reply_to_message.id
    await bot.send_dice(chat_id=update.chat.id, emoji=emoji.GOAL_E_MOJI, disable_notification=True, reply_to_message_id=replyID)

@Client.on_message(filters.private & filters.command(["luck"]))
async def luck_cownd(bot, update):
    replyID = query.from_user.id
    if update.reply_to_message:
        replyID = update.reply_to_message.id
    await bot.send_dice(chat_id=update.chat.id, emoji=emoji.TRY_YOUR_LUCK, disable_notification=True, reply_to_message_id=replyID)
