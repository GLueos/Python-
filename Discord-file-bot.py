#imports all needed libraries
import discord
import os
import time
import pytube
from pytube import YouTube
import glob
import os.path



#sets up the bot
intents = discord.Intents(messages=True, guilds=True, message_content =True)
bot = discord.Client(intents=intents)



#check for messages with yt links   
@bot.event
async def on_message(message):
   #get the video  link
    yt = YouTube(message.content)
    
  # get video using itag vale
    stream = yt.streams.get_by_itag(22)
    stream.download()

    #find the most recent file in python (it will be the video)
    folder_path = r"C:\Users\Your.windows.username\Desktop\Python\Home projects\pybot"
    file_type = r'\*.mp4'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)

    #print it (for tracking and testing)
    print(max_file)

    #Send users info on the selected video while waiting for it to download and upload
    view = "Views =", yt.views
    like = "Description :", yt.description
    await message.channel.send(view)
    await message.channel.send(like)
    time.sleep(5)

    #send the video to the channel the message was sent in
    file = discord.File(max_file, filename= yt.title)
    print("done")
    await message.channel.send(file=file)
    
#runs code with bot token
bot.run("API KEY HERE") 


