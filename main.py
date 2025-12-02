from highrise import BaseBot, SessionMetadata
from dotenv import load_dotenv
import google.generativeai as genai
import os
import asyncio

load_dotenv()

room_ID = os.getenv("room_ID")
bot_token = os.getenv("API_KEY_BOT")

# Configure Gemini
api_key = os.getenv("OPENAI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")


class MyBot(BaseBot):
    
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        # Bot will send a greeting when it starts
        await self.highrise.chat(
            'To use me, always start your message with "Neospire"'
        )
        print("Bot started in room:", session_metadata.room_ID)

    async def on_chat(self, user_id: str, message: str) -> None:
        # Only respond if the message mentions "Neospire"
        if "Neospire" in message:
            # Generate a response using Gemini
            response = model.generate_content(message)
            await self.highrise.chat(user_id,response.text)


