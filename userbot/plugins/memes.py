# Copyright (C) 2019 The Raphielscape Company LLC.
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
# LionX module for having some fun with people.
import asyncio
import random
import re

import requests
from cowpy import cow
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins, MessageEntityMentionName

from userbot import lionx

from ..funcs.managers import eod, eor
from ..helpers import swtmemes
from ..helpers.utils import _lionxutils, parse_pre
from . import BOTLOG, BOTLOG_CHATID, mention

plugin_type = "fun"


async def get_user(event):
    # Get the user from argument or replied message.
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`I don't slap aliens, they ugly AF !!`")
            return None
    return replied_user


@lionx.lion_cmd(
    pattern="(\w+)say ([\s\S]*)",
    command=("cowsay", plugin_type),
    info={
        "header": "A fun art plugin.",
        "flags": [
            "default",
            "beavis",
            "bongcow",
            "budfrogs",
            "bunny",
            "cheese",
            "cower",
            "daemon",
            "dragonandcow",
            "eyes",
            "flamingsheep",
            "ghostbusters",
            "headincow",
            "hellokitty",
            "kiss",
            "kitty",
            "koala",
            "kosh",
            "lukekoala",
            "mechandcow",
            "meow",
            "milk",
            "moofasa",
            "moose",
            "mutilated",
            "ren",
            "satanic",
            "sheep",
            "skeleton",
            "small",
            "sodomized",
            "squirrel",
            "stegosaurus",
            "stimpy",
            "supermilker",
            "surgery",
            "telebears",
            "threeeyes",
            "turkey",
            "turtle",
            "tux",
            "udder",
            "vaderkoala",
            "vader",
            "www",
        ],
        "usage": [
            "{tr}cowsay <text>",
            "{tr}<type>say <text>",
        ],
        "examples": [
            "{tr}squirrelsay LionX",
            "{tr}milksay LionX",
            "{tr}ghostbustersghostbusterssay LionX",
        ],
    },
)
async def univsaye(cowmsg):
    "A fun art plugin."
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)
    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return await eod(cowmsg, "check help menu to know the correct options.")
    cheese = cow.get_cow(arg)
    cheese = cheese()
    await eor(cowmsg, f"`{cheese.milk(text).replace('`', '´')}`")


@lionx.lion_cmd(
    pattern="coin ?([\s\S]*)",
    command=("coin", plugin_type),
    info={
        "header": "Coin flipper.",
        "usage": [
            "{tr}coin <heads/tails>",
            "{tr}coin",
        ],
    },
)
async def _(event):
    "flips a coin."
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "heads":
            await eor(event, "The coin landed on: **Heads**. \n You were correct.")
        elif input_str == "tails":
            await eor(
                event,
                "The coin landed on: **Heads**. \n You weren't correct, try again ...",
            )
        else:
            await eor(event, "The coin landed on: **Heads**.")
    elif r % 2 == 0:
        if input_str == "tails":
            await eor(event, "The coin landed on: **Tails**. \n You were correct.")
        elif input_str == "heads":
            await eor(
                event,
                "The coin landed on: **Tails**. \n You weren't correct, try again ...",
            )
        else:
            await eor(event, "The coin landed on: **Tails**.")
    else:
        await eor(event, r"¯\_(ツ)_/¯")


@lionx.lion_cmd(
    pattern="slap(?:\s|$)([\s\S]*)",
    command=("slap", plugin_type),
    info={
        "header": "To slap a person with random objects !!",
        "usage": "{tr}slap reply/username>",
    },
)
async def who(event):
    "To slap a person with random objects !!"
    replied_user = await get_user(event)
    if replied_user is None:
        return
    caption = await swtmemes.slap(replied_user, event, mention)
    try:
        await eor(event, caption)
    except BaseException:
        await eor(
            event, "`Can't slap this person, need to fetch some sticks and stones !!`"
        )


@lionx.lion_cmd(
    pattern="(yes|no|maybe|decide)$",
    command=("decide", plugin_type),
    info={
        "header": "To decide something will send gif according to given input or ouput.",
        "usage": [
            "{tr}yes",
            "{tr}no",
            "{tr}maybe",
            "{tr}decide",
        ],
    },
)
async def decide(event):
    "To send random gif associated with yes or no or maybe."
    decision = event.pattern_match.group(1).lower()
    message_id = event.reply_to_msg_id or None
    if decision != "decide":
        r = requests.get(f"https://yesno.wtf/api?force={decision}").json()
    else:
        r = requests.get("https://yesno.wtf/api").json()
    await event.delete()
    LIONX = await event.client.send_message(
        event.chat_id, str(r["answer"]).upper(), reply_to=message_id, file=r["image"]
    )
    await _lionxutils.unsavegif(event, LIONX)


@lionx.lion_cmd(
    pattern="shout(?:\s|$)([\s\S]*)",
    command=("shout", plugin_type),
    info={
        "header": "shouts the text in a fun way",
        "usage": [
            "{tr}shout <text>",
        ],
    },
)
async def shout(args):
    "shouts the text in a fun way"
    input_str = args.pattern_match.group(1)
    if not input_str:
        return await eod(args, "__What should i shout?__")
    words = input_str.split()
    msg = ""
    for messagestr in words:
        text = " ".join(messagestr)
        result = [" ".join(text)]
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + " " + "  " * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg += "\n" + result
        if len(words) > 1:
            msg += "\n\n----------\n"
    await eor(args, msg, parse_mode=parse_pre)


@lionx.lion_cmd(
    pattern="owo ?([\s\S]*)",
    command=("owo", plugin_type),
    info={
        "header": "check yourself.",
        "usage": [
            "{tr}owo <text>",
        ],
    },
)
async def faces(owo):
    "UwU"
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await eor(owo, "` UwU no text given! `")
    reply_text = re.sub(r"(r|l)", "w", message)
    reply_text = re.sub(r"(R|L)", "W", reply_text)
    reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = re.sub(r"\!+", " " + random.choice(swtmemes.UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + random.choice(swtmemes.UWUS)
    await eor(owo, reply_text)


@lionx.lion_cmd(
    pattern="clap(?:\s|$)([\s\S]*)",
    command=("clap", plugin_type),
    info={
        "header": "Praise people!",
        "usage": [
            "{tr}clap <text>",
        ],
    },
)
async def claptext(event):
    "Praise people!"
    textx = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif textx.message:
        query = textx.message
    else:
        return await eor(event, "`Hah, I don't clap pointlessly!`")
    reply_text = "👏 "
    reply_text += query.replace(" ", " 👏 ")
    reply_text += " 👏"
    await eor(event, reply_text)


@lionx.lion_cmd(
    pattern="smk(?:\s|$)([\s\S]*)",
    command=("smk", plugin_type),
    info={
        "header": "A shit module for ツ , who cares.",
        "usage": [
            "{tr}smk <text>",
        ],
    },
)
async def smrk(smk):
    "A shit module for ツ , who cares."
    textx = await smk.get_reply_message()
    if smk.pattern_match.group(1):
        message = smk.pattern_match.group(1)
    elif textx.message:
        message = textx.message
    else:
        await eor(smk, "ツ")
        return
    if message == "dele":
        await eor(smk, message + "te the hell" + "ツ")
    else:
        smirk = " ツ"
        reply_text = message + smirk
        await eor(smk, reply_text)


@lionx.lion_cmd(
    pattern="f ([\s\S]*)",
    command=("f", plugin_type),
    info={
        "header": "Pay Respects.",
        "usage": [
            "{tr}f <emoji/character>",
        ],
    },
)
async def payf(event):
    "Pay Respects."
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await eor(event, pay)


@lionx.lion_cmd(
    pattern="wish(?:\s|$)([\s\S]*)",
    command=("wish", plugin_type),
    info={
        "header": "Shows the chance of your success.",
        "usage": [
            "{tr}wish <reply>",
            "{tr}wish <your wish>",
        ],
    },
)
async def wish_check(event):
    "Shows the chance of your success."
    wishtxt = event.pattern_match.group(1)
    chance = random.randint(0, 100)
    if wishtxt:
        reslt = f"**Your wish **__{wishtxt}__ **has been cast.** ✨\
              \n\n__Chance of success :__ **{chance}%**"
    elif event.is_reply:
        reslt = f"**Your wish has been cast. **✨\
                  \n\n__Chance of success :__ **{chance}%**"
    else:
        reslt = "What's your Wish? Should I consider you as Idiot by default ? 😜"
    await eor(event, reslt)


@lionx.lion_cmd(
    pattern="lfy(?:\s|$)([\s\S]*)",
    command=("lfy", plugin_type),
    info={
        "header": "Let me Google that for you real quick !!",
        "usage": [
            "{tr}lfy <query>",
        ],
    },
)
async def _(event):
    "Let me Google that for you real quick !!"
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await eod(
            event, "`either reply to text message or give input to search`", 5
        )
    sample_url = f"https://da.gd/s?url=https://lmgtfy.com/?q={input_str.replace(' ', '+')}%26iie=1"
    response_api = requests.get(sample_url).text
    if response_api:
        await eor(event, f"[{input_str}]({response_api.rstrip()})\n`Thank me Later 🙃` ")
    else:
        return await eod(event, "`something is wrong. please try again later.`", 5)
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"LMGTFY query `{input_str}` was executed successfully",
        )


@lionx.lion_cmd(
    pattern="gbun(?:\s|$)([\s\S]*)",
    command=("gbun", plugin_type),
    info={
        "header": "Fake gban action !!",
        "usage": ["{tr}gbun <reason>", "{tr}gbun"],
    },
)
async def gbun(event):
    "Fake gban action !!"
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n`"
    lionxevent = await eor(event, "**Summoning out le Gungnir ❗️⚜️☠️**")
    await asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for _ in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make meself invulnerable cuz why not xD
        if idd == 1035034432:
            await lionxevent.edit(
                "`Wait a second, This is my master!`\n**How dare you threaten to ban my master nigger!**\n\n__Your account has been hacked! Pay 69$ to my master__ [π.$](tg://user?id=1035034432) __to release your account__😏"
            )
        else:
            jnl = (
                "`Warning!! `"
                "[{}](tg://user?id={})"
                "` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n\n`"
                "**user's Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname is None:
                jnl += "**Victim Nigga's username: ** `Doesn't own a username!`\n"
            else:
                jnl += "**Victim Nigga's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                no_reason = "__Reason: Potential spammer. __"
                jnl += no_reason
            await lionxevent.edit(jnl)
    else:
        mention = "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\nReason: Potential spammer. `"
        await lionxevent.edit(mention)
