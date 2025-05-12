import os

import discord

from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO

from champs.random_champ_weighted import get_random_champs_weighted, make_43_grid_from_champs

load_dotenv()

bot = commands.Bot(command_prefix="champs", intents=discord.Intents.all())

@bot.command()
async def get(ctx, N=40):
    champs = get_random_champs_weighted(N)
    img = make_43_grid_from_champs(champs)
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    file = discord.file.File(img_bytes, filename='champs.png')
    await ctx.send(", ".join(champs), file=file)

bot.run(os.getenv("DISCORD_TOKEN"))
