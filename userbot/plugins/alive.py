import asyncio
import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, lionx, lionxversion

from ..Config import Config
from ..funcs.managers import eor
from ..helpers.functions import check_data_base_heal_th, get_readable_time, lionxalive
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_type = "utils"


@lionx.lion_cmd(
    pattern="lionx$",
    command=("lionx", plugin_type),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}lionx",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lionxevent = await eor(event, "`Checking...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✥"
    LOL_TEXT = gvarstatus("ALIVE_TEXT") or "**⚜ LionX Is Online ⚜**"
    LIONX_IMG = (
        gvarstatus("IALIVE_PIC") or "https://telegra.ph/file/ddc5fa84192641f0915e3.jpg"
    )
    llol = [x for x in LIONX_IMG.split()]
    IPIC = random.choice(llol)
    lal = [x for x in EMOJI.split()]
    EMOTES = random.choice(lal)
    tick = [x for x in LOL_TEXT.split(", ")]
    ALIVE_TEXT = random.choice(tick)
    hell_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = hell_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOTES=EMOTES,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        lionxver=lionxversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if IPIC:
        try:
            await event.client.send_file(
                event.chat_id, IPIC, caption=caption, reply_to=reply_to_id
            )
            await lionxevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await eor(
                lionxevent,
                f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{PIC}`",
            )
    else:
        await eor(
            lionxevent,
            caption,
        )


temp = """{ALIVE_TEXT}
**{EMOTES} Master:** {mention}
**{EMOTES} Uptime :** `{uptime}`
**{EMOTES} Telethon Version :** `{telever}`
**{EMOTES} LionX Version :** `{lionxver}`
**{EMOTES} Python Version :** `{pyver}`
**{EMOTES} Database :** `{dbhealth}`"""


@lionx.lion_cmd(
    pattern="alive$",
    command=("alive", plugin_type),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    a = gvarstatus("ALIVE_EMOJI") or "✥"
    LionX = [x for x in a.split()]
    EMOJI = random.choice(LionX)
    lionx_caption = "**LionX Is Online**\n\n"
    lionx_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    lionx_caption += f"**{EMOJI} LionX Version :** `{lionxversion}`\n"
    lionx_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    lionx_caption += f"**{EMOJI} Uptime :** {uptime}\n"
    lionx_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await event.client.inline_query(Config.BOT_USERNAME, lionx_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


edit_time = 12
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/8bea1e8b8c21e280da185.jpg"
file2 = "https://te.legra.ph/file/d2a5265abdc4e73af1f94.jpg"
file3 = "https://telegra.ph/file/1a13b5a61fb10d275c3ac.jpg"
""" =======================CONSTANTS====================== """
pm_caption = f"**LionX Is Up**\n"
pm_caption += f"**╭────────────**\n"
pm_caption += f"┣»»»『{mention}』«««\n"
pm_caption += f"┣LɪᴏɴXᵘᵇ ~ {lionxversion}\n"
pm_caption += f"┣LɪᴏɴX  ~ [Owner](https://t.me/TeamLionX)\n"
pm_caption += f"┣Support ~ [G𝖗ουρ](https://t.me/LionXsupport)\n"
pm_caption += f"┣Řepô    ~ [Rєρο](https://github.com/TEAMLIONX/LIONX)\n"
pm_caption += f"**╰────────────**\n"


@lionx.lion_cmd(
    pattern="about$",
    command=("about", plugin_type),
    info={
        "header": "To check bot's alive status ",
        "options": "Random Media Automatically Get It",
        "usage": [
            "{tr}about",
        ],
    },
)
async def amireallyalive(yes):
    await yes.get_chat()
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)
    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)
    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok5, file=file3)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok8, file=file2)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok9, file=file3)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await yes.delete()
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await yes.delete()


@lionx.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await lionxalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
