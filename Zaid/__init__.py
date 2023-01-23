import os
from aiohttp import web
from route import web_server
from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging
from pytgcalls import PyTgCalls
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


from Config import Config
BOT_USERNAME = Config.BOT_USERNAME
ASSISTANT_ID = Config.ASSISTANT_ID

Zaid = TelegramClient('Zaid', api_id=Config.API_ID, api_hash=Config.API_HASH)


client = TelegramClient(StringSession(Config.STRING_SESSION), Config.API_ID, Config.API_HASH)
call_py = PyTgCalls(client)

class Bot():
    async def start():
        await Zaid.start(bot_token=Config.BOT_TOKEN)
        await client.start()
        await call_py.start()
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"       
        await web.TCPSite(app, bind_address, 8080).start()     
        print(f"🕸️ Web Started ⚡️⚡️⚡️")
        Zaid.run_until_disconnected()

    async def stop(*args):
        await Zaid.stop()
        await client.stop()
        await call_py.stop()
        print('Bot Stopped Bye')
