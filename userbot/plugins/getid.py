from telethon.utils import pack_bot_file_id

from userbot import lionx
from userbot.funcs.logger import logging

from ..funcs.managers import eod, eor

plugin_type = "utils"

LOGS = logging.getLogger(__name__)


@lionx.lion_cmd(
    pattern="(get_id|id)(?:\s|$)([\s\S]*)",
    command=("id", plugin_type),
    info={
        "header": "To get id of the group or user.",
        "description": "if given input then shows id of that given chat/channel/user else if you reply to user then shows id of the replied user \
    along with current chat id and if not replied to user or given input then just show id of the chat where you used the command",
        "usage": "{tr}id <reply/username>",
    },
)
async def _(event):
    "To get id of the group or user."
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await eod(event, f"`{e}`", 5)
        try:
            if p.first_name:
                return await eor(event, f"The id of the user `{input_str}` is `{p.id}`")
        except Exception:
            try:
                if p.title:
                    return await eor(
                        event, f"The id of the chat/channel `{p.title}` is `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await eor(event, "`Either give input as username or reply to user`")
    elif event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await eor(
                event,
                f"**Current Chat ID : **`{event.chat_id}`\n**From User ID: **`{r_msg.sender_id}`\n**Media File ID: **`{bot_api_file_id}`",
            )

        else:
            await eor(
                event,
                f"**Current Chat ID : **`{event.chat_id}`\n**From User ID: **`{r_msg.sender_id}`",
            )

    else:
        await eor(event, f"**Current Chat ID : **`{event.chat_id}`")
