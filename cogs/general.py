import discord
import textwrap
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("General Category loaded.")
        
    #Commands
    @commands.command()
    @commands.has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx):
        help = discord.Embed(
            title="Help Page",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", #ahahaha
            colour=0xFFA500
        )
        help.add_field(name="General", value="**sp;botinfo** - Info about the bot.\n**sp;kick** - Kick a user.\n**sp;ban** - Ban a user.\n**sp;unban** - Unban a user.\n**sp;purge** - Bulk delete 2-100 messages.")
        help.add_field(name="Fun", value="**sp;ping** - Pong! See the bot's latency.\n**sp;say** - Make me say stuff!\n**sp;kill** - Kill someone. Anyone.\n**sp;blackcat** - Cat pictures from r/blackcats.\n**sp;meme** - Memes from r/memes.")
        await ctx.send(embed=help)
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=5):
        '''
        Purge messages.
        '''
        await ctx.channel.purge(limit=amount)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        '''
        Kick a user.
        '''
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}")
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        '''
        Ban a user.
        '''
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}")
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        '''
        Unban a user.
        '''
        banned_users = await ctx.guild.bans()
        member_name. member_tag = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_tag):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
    @commands.command()
    async def botinfo(self, ctx):
        infoEmbed = discord.Embed(
            title="Stupid Bot",
            colour=0xFFA500,
            description="**Bot Version:** v0.1.0\n**Library:** discord.py **Version:** v1.3.4\n**Developer:** Wayve#3576"
            )
        await ctx.send(embed=infoEmbed)
def setup(client):
    client.add_cog(General(client))