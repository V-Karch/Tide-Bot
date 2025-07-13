import discord
from discord import app_commands
from discord.ext import commands


class Roles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    roles_group = app_commands.Group(name="role", description="role commands")

    @roles_group.command(name="give", description="give a role to a user")
    async def give_role(
        self, interaction: discord.Interaction, user: discord.Member, role: discord.Role
    ) -> None:
        await interaction.response.defer()
        await user.add_roles(role)
        await interaction.followup.send(f'Given role "{role}" to "{user}"')


async def setup(bot: commands.Bot):
    await bot.add_cog(Roles(bot))
