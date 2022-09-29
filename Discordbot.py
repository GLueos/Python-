#imports all needed libraries
import discord
import os
import keyboard
import time
import mouse



#sets up the bot
intents = discord.Intents(messages=True, guilds=True, message_content =True)
bot = discord.Client(intents=intents)
channel = 1021230533654618204
#confrims connection
print("Intialized In 1 seconds")
#functions for keyboard
def my_forward():
         keyboard.press("w")


def my_backward():
        keyboard.press("s")

def my_left():
         keyboard.press("a") 

def my_right():
         keyboard.press("d")

def my_click():
        for i in range(100): mouse.click(button= "left")
        
def my_rightclick():
        for i in range(100): mouse.right_click()
        
def my_e():
         keyboard.press("e")       
        
def my_q():
     keyboard.press("q")
        
def my_1():
         keyboard.press("1")
        
def my_2():
         keyboard.press("2")
         
async def firstroll():
    await bot.send_file(message.channel, 'my_file.png')


        
     

response = 1
# Trigger the functions
@bot.event
async def on_message(message):
	
        if message.content == "w":  my_forward()
        if message.content == "s":  my_backward()
        if message.content == "a":  my_left()
        if message.content == "d":  my_right()
        if message.content == "c":  my_click()
        if message.content == "rc":  my_rightclick()
        if message.content == "e":  my_e()
        if message.content == "q":  my_q()
        if message.content == "1":  my_1()
        if message.content == "2":  my_2() 
        if message.content == "4": firstroll()


#runs code with bot token
bot.run("API KEY HERE") 


