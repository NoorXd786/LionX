#  Copyright (C) 2020  @Simpleboy786
# credits to @TeamLionX (@TeamLionX)
import asyncio
import os
import re

from userbot import lionx

from ..funcs.managers import eod, eor
from ..helpers.utils import reply_id
from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

plugin_type = "fun"


@lionx.lion_cmd(
    pattern="fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", plugin_type),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs LionX ; One of the Popular userbot",
    },
)
async def nekobot(lol):
    "Fake google search meme"
    text = lol.pattern_match.group(1)
    reply_to_id = await reply_id(lol)
    if not text:
        if lol.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await eod(lol, "`What should i search in google.`", 5)
    swte = await eor(lol, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await eod(
            lol,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    swtfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await lol.client.send_file(lol.chat_id, swtfile, reply_to=reply_to_id)
    await swte.delete()
    if os.path.exists(swtfile):
        os.remove(swtfile)


@lionx.lion_cmd(
    pattern="trump(?:\s|$)([\s\S]*)",
    command=("trump", plugin_type),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump LionX is One of the Popular userbot",
    },
)
async def nekobot(lol):
    "trump tweet sticker with given custom text_"
    text = lol.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lol)

    reply = await lol.get_reply_message()
    if not text:
        if lol.is_reply and not reply.media:
            text = reply.message
        else:
            return await eod(lol, "**Trump : **`What should I tweet`", 5)
    swte = await eor(lol, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    swtfile = await trumptweet(text)
    await lol.client.send_file(lol.chat_id, swtfile, reply_to=reply_to_id)
    await swte.delete()
    if os.path.exists(swtfile):
        os.remove(swtfile)


@lionx.lion_cmd(
    pattern="modi(?:\s|$)([\s\S]*)",
    command=("modi", plugin_type),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi LionX is One of the Popular userbot",
    },
)
async def nekobot(lol):
    "modi tweet sticker with given custom text"
    text = lol.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lol)

    reply = await lol.get_reply_message()
    if not text:
        if lol.is_reply and not reply.media:
            text = reply.message
        else:
            return await eod(lol, "**Modi : **`What should I tweet`", 5)
    swte = await eor(lol, "Requesting modi to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    swtfile = await moditweet(text)
    await lol.client.send_file(lol.chat_id, swtfile, reply_to=reply_to_id)
    await swte.delete()
    if os.path.exists(swtfile):
        os.remove(swtfile)


@lionx.lion_cmd(
    pattern="cmm(?:\s|$)([\s\S]*)",
    command=("cmm", plugin_type),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm LionX is One of the Popular userbot",
    },
)
async def nekobot(lol):
    text = lol.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lol)

    reply = await lol.get_reply_message()
    if not text:
        if lol.is_reply and not reply.media:
            text = reply.message
        else:
            return await eod(lol, "`Give text to write on banner, man`", 5)
    swte = await eor(lol, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    swtfile = await changemymind(text)
    await lol.client.send_file(lol.chat_id, swtfile, reply_to=reply_to_id)
    await swte.delete()
    if os.path.exists(swtfile):
        os.remove(swtfile)


@lionx.lion_cmd(
    pattern="kanna(?:\s|$)([\s\S]*)",
    command=("kanna", plugin_type),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna LionX is One of the Popular userbot",
    },
)
async def nekobot(lol):
    "kanna chan sticker with given custom text"
    text = lol.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lol)

    reply = await lol.get_reply_message()
    if not text:
        if lol.is_reply and not reply.media:
            text = reply.message
        else:
            return await eod(lol, "**Kanna : **`What should i show you`", 5)
    swte = await eor(lol, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    swtfile = await kannagen(text)
    await lol.client.send_file(lol.chat_id, swtfile, reply_to=reply_to_id)
    await swte.delete()
    if os.path.exists(swtfile):
        os.remove(swtfile)


@lionx.lion_cmd(
    pattern="tweet(?:\s|$)([\s\S]*)",
    command=("tweet", plugin_type),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; LionX is One of the Popular userbot",
    },
)
async def nekobot(lol):
    "The desired person tweet sticker with given custom text"
    text = lol.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lol)

    reply = await lol.get_reply_message()
    if not text:
        if lol.is_reply and not reply.media:
            text = reply.message
        else:
            return await eod(
                lol,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await eod(
            lol,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    swte = await eor(lol, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    swtfile = await tweets(text, username)
    await lol.client.send_file(lol.chat_id, swtfile, reply_to=reply_to_id)
    await swte.delete()
    if os.path.exists(swtfile):
        os.remove(swtfile)
