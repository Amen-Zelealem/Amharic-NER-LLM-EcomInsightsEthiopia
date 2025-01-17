import os
import asyncio
import logging
from telethon import TelegramClient
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("TelegramMessageFetcherTest")

# Load environment variables
load_dotenv()

# Telegram API credentials
API_ID = os.getenv("api_id")
API_HASH = os.getenv("api_hash")

if not API_ID or not API_HASH:
    logger.error("API ID or API Hash not found. Please check your .env file.")
    exit("Error: Missing credentials in .env file.")

CHANNEL_USERNAMES = ["@ethio_brand_collection"]


async def fetch_messages(client, channel_username, limit=5):
    """
    Fetch a limited number of messages from a Telegram channel for testing.
    """
    logger.info(f"Fetching messages from: {channel_username}")
    try:
        messages = [
            msg.text
            for msg in await client.iter_messages(channel_username, limit=limit)
        ]
        logger.info(f"Fetched {len(messages)} messages.")
        return messages
    except Exception as e:
        logger.error(f"Error fetching messages: {e}")
        return []


async def main():
    """
    Main function to run the test.
    """
    logger.info("Starting Telegram client for test...")
    async with TelegramClient("test_session", API_ID, API_HASH) as client:
        for channel in CHANNEL_USERNAMES:
            messages = await fetch_messages(client, channel)
            logger.info(f"Messages from {channel}: {messages}")


if __name__ == "__main__":
    asyncio.run(main())
