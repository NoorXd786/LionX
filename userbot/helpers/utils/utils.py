import asyncio
import functools
import shlex
from typing import Tuple

from telethon import functions, types

from ...funcs.logger import logging

LOGS = logging.getLogger(__name__)

# executing of terminal commands
async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


def run_sync(func, *args, **kwargs):
    return asyncio.get_event_loop().run_in_executor(
        None, functools.partial(func, *args, **kwargs)
    )


def runasync(func: callable):
    """Run async functions with the right event loop."""
    asyncio.get_event_loop()
    return loop.run_until_complete(func)


def run_async(loop, coro):
    return asyncio.run_coroutine_threadsafe(coro, loop).result()


async def unsavegif(event, LIONX):
    try:
        await event.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=LIONX.media.document.id,
                    access_hash=LIONX.media.document.access_hash,
                    file_reference=LIONX.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        LOGS.info(str(e))
