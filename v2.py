#!/usr/bin/python3
import logging
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import discord, os, requests, nmap, time, socket, subprocess, sys, datetime, psutil, random;from random import randint
import platform;from subprocess import PIPE, run;from io import StringIO
print("\n\nAll Imports Success\n")
logger = logging.getLogger();logger.setLevel(logging.CRITICAL);print("\nLogging Enabled!")

class settings:
    token = "NjA4MDA1NTI2MTg1MzEyMjY2.XUtC3g.V8Tl_Ngh0juwmkBpZMxGyNOOf7A"
    
client = discord.Client()
chatbot = ChatBot("Temper")

#class knowledge:
#    anomalies = [line.rstrip('\n') for line in open("delims.dat")]

class s:
    null = ""
    s = " "
    n = "\n" 
    dialog_size = str(os.path.getsize("Dialog.dat"))
    sentence_size = str(os.path.getsize("sentence_tokenizer.pickle"))
    db_size = str(os.path.getsize("db.sqlite3"))
    host = socket.gethostname()
    dt = datetime.datetime.now()
    dts = f"{dt}"
    arch = str(platform.machine())
    plat = str(platform.platform())
    ver = str(platform.version())
    cpu = str(platform.processor())
    cpu_use = str(psutil.cpu_percent())
    mem = str(psutil.virtual_memory())
    version = str(f"""
       >>>>Info/Version<<<<

 Intelligent Agent:
 Temper v.0.0.9.0 (HexButler v0.0.5.5) - CyberCreature Security

**Release Date:**
Updated: [8-7-2019] @ 1:41am  //  Time Now: {dts}

AI Stats:
Dialog Database: {dialog_size} bytes
Sentence/Tokenization: {sentence_size} bytes
Sentient Database(sqlite3): {db_size} bytes 

System:
Platform: {plat}
Version: {ver}
Unit: {host}
Architecture: {arch}
CPU: {cpu}
Usage: {cpu_use}%
Memory: {mem}
Local Time: {dts}

""")
print("ChatBot: Initializing")
trainer = ListTrainer(chatbot)
print('\nSuccess')
print("Loading Training Data")
trainer.train([line.rstrip('\n') for line in open("dialog.dat", "r", encoding="utf8")])#####################################################################
print('\nSuccess\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

@client.event
async def on_ready():
    print('-\n[Ok] - Succesfully logged in as {0.user}'.format(client))
    print(s.version)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    bError = False
    
    if message.content.startswith('-v') or message.content.startswith('version') or message.content.startswith('dev'):
        await message.delete()
        dialog_size1 = str(os.path.getsize("Dialog.dat"))
        sentence_size1 = str(os.path.getsize("sentence_tokenizer.pickle"))
        db_size1 = str(os.path.getsize("db.sqlite3"))
        host1 = socket.gethostname()
        dt1 = datetime.datetime.now()
        dts1 = f"{dt1}"
        arch1 = str(platform.machine())
        plat1 = str(platform.platform())
        ver1 = str(platform.version())
        cpu1 = str(platform.processor())
        cpu_use1 = str(psutil.cpu_percent())
        mem1 = str(psutil.virtual_memory())
        version1 = str(f"""
    __**Info/Stats**__

    **Intelligent Agent:**
    ```yaml
     Temper v.0.1.0.0  - CyberCreature Security
     (Chatterbot API)
     ```
    **Release Date:**
    ```yaml
    Updated: [8-7-2019] @ 1:41am
    Now: {dts1}
    ```
    **AI Stats:**
    ```yaml
    Dialog Database: {dialog_size1} bytes
    Sentence/Tokenization: {sentence_size1} bytes
    Sentient Database(sqlite3): {db_size1} bytes 
    ```
    **System:**
    ```yaml
    Platform: {plat1}
    Version: {ver1}
    Unit/Hostname: {host1}
    Architecture: {arch1}
    CPU: {cpu1}
    CPU Usage: {cpu_use1}%
    Virtual Memory: {mem1}
    Local Time: {dts1}
    ```
    """)
        await message.channel.send(version1) 

    if message.content:
        parsed = message.content.replace('^', '').replace('\\', '').replace("*",'').replace("#", '').replace("<", '').replace(">", '').replace("@",'').replace("ツ",'').replace("0",'').replace("1",'').replace("2",'').replace("3",'').replace("4",'').replace("5",'').replace("6",'').replace("7",'').replace("8",'').replace("9",'')#pruning/parsing our input
        try:
            a = open("dialog.dat", "a", encoding="utf8") #Aknowledge and save to db.
            a.write(f'{parsed}\n')
            a.close()
        except Exception as f1:
            print("First write to mem. failed!\n"+str(f1))
            await message.channel.send("Sorry, I've lost our conversation :(\n```yaml\nError Flag 1:\n"+str(f1)+'\n```')
            bError = True
            pass
        print(parsed)
        if bError == False:
            try:
                response = str(chatbot.get_response(parsed)) #Grabbing a response then sending it back
                await message.channel.send(f"{message.author} {response}")
            except Exception as f2:
                print("Response failed!\n "+str(f2))
                await message.channel.send("Sorry, I've failed to come up with a response :(\n```yaml\nError Flag 2:\n"+str(f2)+'\n```')
                bError = True
                pass

        #if bError == False:
            #dice = randint(1,2) # Randomize reccollection of our own response   - 2nd write to mem.
            #if dice == 2:
                #b = open("dialog.dat","a", encoding="utf8")
                #b.write(f'{response}\n')
                #b.close()

        elif bError == True:
            pass       
    else:
        pass
    
try:
    client.run(settings.token)
except Exception as eee:
    print(str(eee))
    pass




#
        #pruned = message.content.split(' ', 1)[1]
        #inp = str(pruned)
