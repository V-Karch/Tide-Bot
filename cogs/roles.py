import discord
from discord import app_commands
from discord.ext import commands


class Roles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    roles_group = app_commands.Group(name="role", description="role commands")

    @roles_group.command(name="give", description="give a role to a user")
    @app_commands.describe(
        user="A server member to give a role to",
        role="A server role to apply to a server member",
    )
    async def give_role(
        self, interaction: discord.Interaction, user: discord.Member, role: discord.Role
    ) -> None:
        await interaction.response.defer()
        await user.add_roles(role)
        await interaction.followup.send(f'Given role "{role}" to "{user}"')

    @roles_group.command(name="list", description="list all roles a user has")
    @app_commands.describe(user="A server member whose roles you want to see")
    async def list_roles(self, interaction: discord.Interaction, user: discord.Member):
        await interaction.response.send_message(user.mention)


async def setup(bot: commands.Bot):
    await bot.add_cog(Roles(bot))
