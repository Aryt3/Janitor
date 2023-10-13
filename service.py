import os
import discord 
from discord.ext import commands
from model import models
from model.database import DBSession

auth_token = os.environ.get("DC_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)  

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')

@bot.event
async def on_message(message: discord.Message):
    db = DBSession()
    try:
        msg_author = db.query(models.User).get(str(message.author.id))
        if not msg_author:
            new_user = models.User(
                id=message.author.id, name=message.author.name
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)

        new_msg = models.Msg(
            author_id=message.author.id, message=message.content
        )
        db.add(new_msg)
        db.commit()
        db.refresh(new_msg)
    finally:
        db.close()

bot.run(auth_token)

