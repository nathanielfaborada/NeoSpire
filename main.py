from highrise import BaseBot, SessionMetadata, User, CurrencyItem, Item
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
        

    async def on_chat(self, user_id: str, message: str) -> None:
        if "Neospire" in message:
            # Ask Gemini to generate a short response
            prompt = f"Reply to this in exactly 10 words, making sense: {message}"
            response = model.generate_content(prompt)
            
            # Optional: ensure 10 words max
            words = response.text.split()
            short_response = " ".join(words[:5])
            
            await self.highrise.chat(short_response)
            print(f"Responded to {user_id} with: {short_response}")
            
    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
        print (f"{sender.username} tipped {receiver.username} an amount of {tip.amount}")



