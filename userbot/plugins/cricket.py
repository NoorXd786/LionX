"""
Created by @TeamLionX
plugin for @LionXsupport
"""

from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import eor, lionx, reply_id

plugin_type = "extra"


@lionx.lion_cmd(
    pattern="score$",
    command=("score", plugin_type),
    info={
        "header": "To see the score of an ongoing match.",
        "usage": "{tr}score",
    },
)
async def _(event):
    "To see the score of an ongoing match."
    chat = "@cricbuzz_bot"
    reply_to_id = await reply_id(event)
    lionxevent = await eor(event, "```Gathering info...```")
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message("/score")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await lionxevent.edit("Unblock @cricbuzz_bot & try again")
            return
        if respond.text.startswith("I can't find that"):
            await lionxevent.edit("sorry i can't find it")
        else:
            await lionxevent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )


@lionx.lion_cmd(
    pattern="cric ([\s\S]*)",
    command=("cric", plugin_type),
    info={
        "header": "To see the scoreboard or commentary of a match",
        "description": "To check commands showed in {tr}score cmd that is for getting scoreboard or commentary.",
        "usage": "{tr}cric <command showed in {tr}score>",
        "examples": "{tr}cric /scorecard_30....",
    },
)
async def _(event):
    "To see the scoreboard or commentary of a match"
    details = event.pattern_match.group(1)
    chat = "@cricbuzz_bot"
    reply_to_id = await reply_id(event)
    lionxevent = await eor(event, "```Gathering info...```")
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message(f"{details}")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await lionxevent.edit("Unblock @cricbuzz_bot & try again")
            return
        if respond.text.startswith("I can't find that"):
            await lionxevent.edit("sorry i can't find it")
        else:
            await lionxevent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )
