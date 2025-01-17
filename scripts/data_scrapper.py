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


async def fetch_messages(client, channel):
    messages = []
    try:
        async for message in client.iter_messages(channel, limit=100):
            messages.append(message.text)
    except Exception as e:
        logger.error(f"Failed to fetch messages from {channel}: {e}")
    return messages

async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        all_messages = []
        for channel in channel_usernames:
            messages = await fetch_messages(client, channel)
            all_messages.extend(messages)

        save_messages_to_csv(all_messages)

def save_messages_to_csv(messages, filename='telegram_messages.csv'):
    if os.path.exists(filename):
        choice = input(f"File {filename} exists. Overwrite? (Y/N): ").lower()
        if choice != 'y':
            logger.info("Operation cancelled.")
            return

    df = pd.DataFrame(messages, columns=['messages'])
    df.to_csv(filename, index=False)
    logger.info(f"Messages saved to {filename}.")


