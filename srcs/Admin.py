import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member:
            await member.kick(reason=reason)
            await ctx.send(f"{member.mention} has been kicked for {reason}.")
        else:
            await ctx.send("Please specify a member to kick.")

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member:
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} has been banned for {reason}.")
        else:
            await ctx.send("Please specify a member to ban.")

    @commands.command(name="mute")
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Mute")  
        if mute_role:
            await member.add_roles(mute_role)
            await ctx.send(f"{member.mention} was silent.")
        else:
            mute_role = await ctx.guild.create_role(name="Mute")
            await ctx.invoke(self.mute, member)

async def setup(bot):
    await bot.add_cog(Admin(bot))
