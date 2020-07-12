import praw
import discord
import os
import random
from discord.ext import commands

reddit = praw.Reddit(client_id="clientid",
                     client_secret="clientsecret",
                     user_agent='Stupid-Bot')

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Category loaded.")

    #Commands
    @commands.command()
    async def say(self, ctx, *args):
        '''
        Make me say stuff!
        '''
        msg = ' '.join(args)
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def kill(self, ctx, member : discord.Member):
        if member.guild.id != ctx.guild.id:
            return
        if (member.id == ctx.message.author.id):
            return await ctx.send("Done, you're dead. Mention someone for me to kill next time.")
        messages = [f"{ctx.message.author.display_name} killed {member.display_name} by smashing their skull with a hammer.", 
                    f"{ctx.message.author.display_name} held {member.display_name}'s head underwater until they stopped moving.", 
                    f"{member.display_name} died of a heart attack after {ctx.message.author.display_name} scared them.",
                    f"{member.display_name} couldn't even take one punch from {ctx.message.author.display_name} before dying.",
                    f"{ctx.message.author.display_name} hit {member.display_name} with his car",
                    f"{ctx.message.author.display_name} cut {member.display_name} in half with a chainsaw"]
        await ctx.send(random.choice(messages))
    @commands.command()
    async def blackcat(self, ctx):
        cat_submissions = reddit.subreddit('blackcats').new()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in cat_submissions if not x.stickied)
            submissionurl = submission.url
            if "imgur" in submission.url:
                submissionurl = submission.url + ".jpg"
        catembed = discord.Embed(
            title="Meow",
            colour=random.randint(0, 0xffffff)
            )
        #print(submissionurl) 
        if not submissionurl.endswith("jpg"):
            img = random.choice(os.listdir("./images/"))
            catembed = discord.Embed(
                title="Meow",
                colour=random.randint(0, 0xffffff)
                )
            file = discord.File("./images/"+img, filename="image.jpg")
            catembed.set_image(url="attachment://image.jpg")
            await ctx.send(file=file, embed=catembed)
            return
        catembed.set_image(url=submissionurl)
        await ctx.send(embed=catembed)
    @commands.command()
    async def meme(self, ctx):
        meme_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in meme_submissions if not x.stickied)
        memeembed = discord.Embed(
            title=submission.title,
            colour=random.randint(0, 0xffffff)
            )
        #print(submission.title) 
        memeembed.set_image(url=submission.url)
        await ctx.send(embed=memeembed)

def setup(client):
    client.add_cog(Fun(client))