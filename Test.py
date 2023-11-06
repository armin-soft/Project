from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.enums import MessageMediaType
import random , os

app = Client(
name=   'OnlineBOT',
api_id= 5165750,
api_hash= '37e719674822342f62b7a933e41f17ef'
)
admin = 592526230

@app.on_message(filters.private and filters.text)
async def running(c: Client, m: Message) :
text =  m.text
from_id =   m.from_user.id
if from_id == admin :
if text == 'ربات' or text == 'bot' or text == '/bot':
await m.reply_text('<b>Bot is Running</b>')

if 'https://t.me/' in text :
send =  await m.reply_text('<b>Wait a moment ..</b>')
rand =  random.randint(1000, 9999999)
link =  text
link =  link.replace('https://t.me/', '').replace('c/', '').replace('?single', '')
split = link.split('/')
try :
if int(split[0]) :
chat_id =   str('-100' + split[0])
except Exception :
chat_id =   str('@' + split[0])
message_id =int(split[1])
caption =   f"☑️ Downloaded successful!"
try :
await app.get_chat(chat_id=chat_id)
except Exception as Error :
await m.reply_text(Error)
else :
info =  await app.get_messages(chat_id=chat_id, message_ids=message_id)
format =None
if info.media == MessageMediaType.VIDEO :
format ='mp4'
if info.media == MessageMediaType.PHOTO :
format ='jpg'
if format is not None:
try :
await app.edit_message_text(chat_id=admin, message_id=send.id, text='<b>📥 Downloading ..</b>')
await app.download_media(message=info, file_name=f'downloaded-{rand}.{format}')
path = f'downloads/downloaded-{rand}.{format}'
await app.edit_message_text(chat_id=admin, message_id=send.id, text='<b>🗳 sending ..</b>')
if format == 'mp4' :
await app.send_video(chat_id=admin, video=path, caption=caption)
if format == 'jpg' :
await app.send_photo(chat_id=admin, photo=path, caption=caption)
except Exception as error:
print(error)
await m.reply_text('<b>Video or Photo not found!</b>')
else :
os.remove(path)
else :
await m.reply_text('<b>Video or Photo not found!</b>')
finally :
await app.delete_messages(chat_id=admin, message_ids=send.id)

@app.on_message(filters.photo)
async def onphoto(c: Client, m: Message) :
try :
if m.photo.ttl_seconds :
rand = random.randint(1000, 9999999)
local = f"downloads/photo-{rand}.png"
await app.download_media(message=m, file_name=f"photo-{rand}.png")
await app.send_photo(chat_id=admin, photo=local, caption=f"🔥 New timed image {m.photo.date} | time: {m.photo.ttl_seconds}s")
os.remove(local)
except :
pass

@app.on_message(filters.video)
async def onvideo(c: Client, m: Message) :
try :
if m.video.ttl_seconds :
rand = random.randint(1000, 9999999)
local = f"downloads/video-{rand}.mp4"
await app.download_media(message=m, file_name=f"video-{rand}.mp4")
await app.send_video(chat_id=admin, video=local, caption=f"🔥 New timed video {m.video.date} | time: {m.video.ttl_seconds}s")
os.remove(local)
except :
pass

app.start(), print("Bot is Running , @FaceAi_Tm"), idle(), app.stop()