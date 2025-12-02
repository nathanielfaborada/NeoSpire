import random
import asyncio
from highrise import BaseBot, SessionMetadata, User, CurrencyItem, Item, Position, AnchorPosition
from dotenv import load_dotenv
import google.generativeai as genai
import os

from emote import free_emotes

load_dotenv()

room_ID = os.getenv("room_ID")
bot_token = os.getenv("API_KEY_BOT")

# Configure Gemini
api_key = os.getenv("OPENAI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")


class MyBot(BaseBot):

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        # Initial greeting when bot starts
        await self.highrise.chat(
            'Ask me anything, always start your message with "Neospire"'
        )
        print("Bot started in room:", session_metadata)

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        # Greet the new user
        await self.highrise.chat(f"Welcome {user.username}!")
        print(f"{user.username} joined at {position}")

        # Bot performs a random free emote
        emote_id = random.choice(free_emotes)
        await self.highrise.emote(emote_id)
        print(f"Bot performed emote {emote_id} for user join.")

    async def on_chat(self, user: User, message: str) -> None:
        # Respond only if user starts message with "Neospire"
        if "Neospire" in message:
            prompt = f"Reply to this in exactly 5 words, making sense: {message}"
            response =  model.generate_content(prompt)

            # Ensure exactly 5 words
            words = response.text.split()
            short_response = " ".join(words[:5])

            await self.highrise.chat(short_response)
            print(f"Responded to {user.username} with: {short_response}")

    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
        print(f"{sender.username} tipped {receiver.username} an amount of {tip.amount}")


