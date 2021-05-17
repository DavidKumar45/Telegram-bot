from pyrogram import Client, filters

from database.userchats import get_all_chats
from vars import var


@Client.on_message(filters.command("broadcast") & filters.user(int(var.OWNER_ID)))
async def bcast(client, message):
    if message.reply_to_message:
        MSG = message.reply_to_message
    else:
        return await message.reply_text("`Reply to a Message !`")
    ALLCHATS = get_all_chats()
    SUCE = 0
    FAIL = 0
    for chat in ALLCHATS:
        try:
            await MSG.copy(chat)
            SUCE += 1
        except Exception:
            FAIL += 1
    await message.reply_text(
        f"Successfully Broadcasted to {SUCE} Chats\nFailed - {FAIL} Chats !"
    )


@Client.on_message(filters.command("stats") & filters.user(int(var.OWNER_ID)))
async def gistat(_, message):
    al = get_all_chats()
    await message.reply_text(f"Total Chats in Database - {len(al)}", quote=True)
