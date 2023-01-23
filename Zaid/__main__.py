import asyncio
import telethon
import glob
from pathlib import Path
from Zaid.utils import load_plugins
import logging
from Zaid import Bot, Zaid, call_py
from Zaid import client, ASSISTANT_ID
from Zaid.plugins.autoleave import leave_from_inactive_call


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Zaid/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))


async def start_bot():
     await Zaid.start(bot_token=Config.BOT_TOKEN)
     await client.start()
     await call_py.start()
     print("[INFO]: LOADING ASSISTANT DETAILS")
     botme = await client.get_me()
     botid = telethon.utils.get_peer_id(botme)
     print(f"[INFO]: ASSISTANT ID {botid}")
     await asyncio.create_task(leave_from_inactive_call())
     app = web.AppRunner(await web_server())
     await app.setup()
     bind_address = "0.0.0.0"       
     await web.TCPSite(app, bind_address, 8080).start()     
     print(f"🕸️ Web Started ⚡️⚡️⚡️")


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

print("[INFO]: SUCCESSFULLY STARTED BOT!")
print("[INFO]: VISIT @TheUpdatesChannel")


if __name__ == "__main__":
    Zaid.run_until_disconnected()
