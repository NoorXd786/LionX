from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ..helpers.functions import age_verification
from ..helpers.nsfw import unsave_gif
from ..helpers.utils import reply_id
from . import lionx, useless

plugin_type = "useless"


@lionx.lion_cmd(
    pattern="hpic$",
    command=("hpic", plugin_type),
    info={
        "header": "This Is 18+ Plugin",
        "usage": "{tr}hpic",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Lolis")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐 I Cant Find that")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@lionx.lion_cmd(
    pattern="hfutanari$",
    command=("hfutanari", plugin_type),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hfutanari",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Futanari")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐 I Cant Find that")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@lionx.lion_cmd(
    pattern="hshota$",
    command=("hshota", plugin_type),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hshota",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Shota")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@lionx.lion_cmd(
    pattern="hvideo$",
    command=("hvideo ", plugin_type),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hvideo",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Hentai Videos")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@lionx.lion_cmd(
    pattern="hoppai$",
    command=("hoppai", plugin_type),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hoppai",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Oppai")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@lionx.lion_cmd(
    pattern="htrap$",
    command=("htrap", plugin_type),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}htrap",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Trap")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@lionx.lion_cmd(
    pattern="hbdsm$",
    command=("hbdsm", plugin_type),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hbdsm",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "BDSM")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@lionx.lion_cmd(
    pattern="hfurry$",
    command=("hfurry", plugin_type),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hfurry",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Furry")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@lionx.lion_cmd(
    pattern="hgif$",
    command=("hgif", plugin_type),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hgif",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "GIF Hentai")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@lionx.lion_cmd(
    pattern="hcosplay$",
    command=("hcosplay", plugin_type),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hcosplay",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Cosplay")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)
