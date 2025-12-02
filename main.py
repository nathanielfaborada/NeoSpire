from highrise import BaseBot, SessionMetadata
from dotenv import load_dotenv
import os


load_dotenv()

room_ID = os.getenv("room_ID")
bot_token = os.getenv("API_KEY_BOT")


# NeoSpire Bot will use OpenAI API for chatting
api_key = os.getenv("OPENAI_API_KEY")


class MyBot(BaseBot):
    
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.chat("Hello, world!")
        print(session_metadata)
        
    
