import os
import asyncio
import logging
import sys
import pandas as pd
from telethon import TelegramClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

if not api_id or not api_hash:
    sys.exit("💥API credentials missing. Check your .env file.")

channel_usernames = [
    "@ethio_brand_collection",
    "@ZemenExpress",
    "@AwasMart",
    "@modernshoppingcenter",
    "@Shewabrand",
]


async def main():
    async with TelegramClient("session_name", api_id, api_hash) as client:
        all_messages = []
        for channel in channel_usernames:
            async for message in client.iter_messages(channel, limit=100):
                all_messages.append(message.text)

        df = pd.DataFrame(all_messages, columns=["messages"])
        df.to_csv("telegram_messages.csv", index=False)
