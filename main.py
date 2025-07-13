import typing
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


def main():

    bot_kwargs: typing.Dict[str, typing.Any] = {
        "intents": discord.Intents.all(),
        "command_prefix": "!",
        "help_command": None,
    }

    bot: commands.Bot = commands.Bot(**bot_kwargs)

    token = read_token()

    print(read_logo())
    bot.run(token)


if __name__ == "__main__":
    main()
