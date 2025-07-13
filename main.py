import os
import typing
import asyncio
import discord
from discord.ext import commands


def read_logo() -> str:
    with open("logo.txt", "r") as f:
        logo = f.read()

    return "\033[38;2;132;187;246m" + logo + "\033[0m"


def read_token() -> str:
    with open("token.txt", "r") as f:
        token = f.read().strip()

    return token


async def main():

    bot_kwargs: typing.Dict[str, typing.Any] = {
        "intents": discord.Intents.all(),
        "command_prefix": "!",
        "help_command": None,
    }

    bot: commands.Bot = commands.Bot(**bot_kwargs)

    token = read_token()

    for cog in os.listdir("cogs"):
        if cog.endswith(".py"):
            print(f'Loading extension "{cog}"...')
            await bot.load_extension("cogs." + cog.replace(".py", ""))

    print(read_logo())
    await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())
