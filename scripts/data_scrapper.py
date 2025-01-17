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

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Connecting to Telegram client...")
    async with TelegramClient('session_name', api_id, api_hash) as client:
        logger.info("Client connected successfully.")
        all_messages = []
        for channel in channel_usernames:
            try:
                logger.info(f"Fetching messages from {channel}...")
                async for message in client.iter_messages(channel, limit=100):
                    all_messages.append(message.text)
            except Exception as e:
                logger.error(f"Failed to fetch messages from {channel}: {e}")

        logger.info(f"Fetched {len(all_messages)} messages.")
        df = pd.DataFrame(all_messages, columns=['messages'])
        df.to_csv('telegram_messages.csv', index=False)
        logger.info("Messages saved to telegram_messages.csv.")

