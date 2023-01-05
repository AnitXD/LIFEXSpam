import asyncio
import importlib
from altron import ALL_MODULES
from pyrogram import idle
from config import client, client2, client3, client4, client5, client6, client7, client8, client9, client10


async def main():
    if client:
        try:
            await client.start()
            await client.join_chat("TheAltron")
            await client.join_chat("AltronChats")
            await client.join_chat("AboutShailendra")
            await client.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client2:
        try:
            await client2.start()
            await client2.join_chat("TheAltron")
            await client2.join_chat("AltronChats")
            await client2.join_chat("AboutShailendra")
            await client2.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client3:
        try:
            await client3.start()
            await client3.join_chat("TheAltron")
            await client3.join_chat("AltronChats")
            await client3.join_chat("AboutShailendra")
            await client3.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client4:
        try:
            await client4.start()
            await client4.join_chat("TheAltron")
            await client4.join_chat("AltronChats")
            await client4.join_chat("AboutShailendra")
            await client4.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client5:
        try:
            await client5.start()
            await client5.join_chat("TheAltron")
            await client5.join_chat("AltronChats")
            await client5.join_chat("AboutShailendra")
            await client5.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client6:
        try:
            await client6.start()
            await client6.join_chat("TheAltron")
            await client6.join_chat("AltronChats")
            await client6.join_chat("AboutShailendra")
            await client6.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client7:
        try:
            await client7.start()
            await client7.join_chat("TheAltron")
            await client7.join_chat("AltronChats")
            await client7.join_chat("AboutShailendra")
            await client7.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client8:
        try:
            await client8.start()
            await client8.join_chat("TheAltron")
            await client8.join_chat("AltronChats")
            await client8.join_chat("AboutShailendra")
            await client8.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client9:
        try:
            await client9.start()
            await client9.join_chat("TheAltron")
            await client9.join_chat("AltronChats")
            await client9.join_chat("AboutShailendra")
            await client9.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client10:
        try:
            await client10.start()
            await client10.join_chat("TheAltron")
            await client10.join_chat("AltronChats")
            await client10.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    for all_module in ALL_MODULES:
        importlib.import_module("altron" + all_module)
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
