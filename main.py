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
            'Ask me anything, always start your message with "Neospire"'
        )
        print("Bot started in room:", session_metadata)

    async def on_user_join(self, user, position) -> None:
        # Greet new user
        await self.highrise.chat(
            f"Welcome {user.display_name}! Ask me anything, start with 'Neospire'"
        )

    async def on_chat(self, user, message: str) -> None:
        # Check if message is meant for Neospire
        if "Neospire" in message:
            prompt = f"Reply to this in exactly 10 words, making sense: {message}"
            
            # Await the async call
            response = await model.generate_content(prompt)
            
            # Ensure exactly 10 words
            words = response.text.split()
            short_response = " ".join(words[:10])
            
            await self.highrise.chat(short_response)

