import discord

import capy_discord
from capy_discord.bot import Bot
from capy_discord.config import settings


def main() -> None:
    """Main function to run the application."""
    capy_discord.instance = Bot(command_prefix=settings.prefix, intents=discord.Intents.all())
    capy_discord.instance.run(settings.token)


main()
