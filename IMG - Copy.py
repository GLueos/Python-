#this is a discord bot I made wich acts as a wrapper for The dreamstudio Ai image generator, so you can use it in discord. To use it just get an api key from dreamstudio and an api key from discord, then configure the files correctly.

import discord
intents = discord.Intents(messages=True, guilds=True, message_content =True)
bot = discord.Client(intents=intents)
import glob
import os.path
from IPython.display import display
import io
import os
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
stability_api = client.StabilityInference(
    key='Just add a dremstudio api key here', 
    verbose=True,
)
@bot.event
async def on_message(message):
     if (message.author.bot):
         print("sent message")
     else:
        if "IMG" in message.content:
             
               
               answers = stability_api.generate(
        		prompt= (message.content)
   		 )
               for resp in answers:
                    for artifact in resp.artifacts:
                         if artifact.type == generation.ARTIFACT_IMAGE:
                             img = Image.open(io.BytesIO(artifact.binary))
                             img = img.save("img.jpg")
                             image = Image.open("img.jpg")
                             image.show()
                             file = discord.File(r"C:\Users\your-user-name-here\Desktop\make-a-folder-for-the-bot\img.jpg", filename= "img.jpg")
                             await message.channel.send(file=file)

bot.run("Add you discord api key here") 
