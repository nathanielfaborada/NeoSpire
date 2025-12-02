from highrise import BaseBot, SessionMetadata
from dotenv import load_dotenv
import asyncio
import os

from .outfit import random_outfit


load_dotenv()

room_ID = os.getenv("room_ID")
bot_token = os.getenv("API_KEY_BOT")


class MyBot(BaseBot):

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.chat("NeoSpire online! Random outfit enabled.")
        print(session_metadata)
        # Start background task
        asyncio.create_task(self.outfit_loop())
        

    async def outfit_loop(self):
        while True:
            try:
                outfit = random_outfit()
                await self.highrise.change_outfit(outfit=outfit)
                await self.highrise.chat("New outfit applied! 🎽👖👟")

            except Exception as e:
                print("Outfit error:", e)

            await asyncio.sleep(3600)  # 3600 seconds = 1 hour
