from highrise import BaseBot, SessionMetadata
from dotenv import load_dotenv
import os

load_dotenv()

room_ID = os.getenv("room_ID")
bot_token = os.getenv("API_KEY_BOT")


class MyBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot has started!")
        print(session_metadata)
