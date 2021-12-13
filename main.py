import asyncio
from pytgcalls import idle
from driver.zeal import call_py, bot

async def mulai_bot():
    print("[ZEAL]: STARTING BOT CLIENT")
    await bot.start()
    print("[ZEAL]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[ZEAL]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())
