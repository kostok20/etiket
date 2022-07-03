import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

emoji_calisan = []

anlik_calisan = []

tekli_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("●** SELAM ❤️**\n\n● **  GRUPLARDA ÜCRETSİZ ETİKETLEME BOTUYUM . . !** \n\n● **NASIL ÇALIŞTIĞIMI ÖĞRENMEK İÇİN LÜTFEN  /help YAZIN  . . !**",
                    buttons=(
                   
		      [Button.url('🎉  Beni Gruba Ekle  🎉', 'https://t.me/BugsBunyEtiket_bot?startgroup=a')],
                      [Button.url('😎  SAHİBİM  😎', 'https://t.me/slmBATU')],
                      
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "📝 **ETİKET KOMUTLARI **\n\n**» /utag < MESAJINIZ > \nGRUPTAKİ KULLANICILARI 5'Lİ ETİKET ATAR .  .  !**\n\n**» /tag  < MESAJINIZ > \nGRUPTAKİ KULLANICILARI TEK TEK ETİKET ATAR . . !**\n\n**» /cancel => ETİKETLEME İŞLEMİNİ DURDURUR . . !**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🎉  Beni Gruba Ekle  🎉', 'https://t.me/BugsBunyEtiket_bot?startgroup=a')],
                      [Button.url('😎  SAHİBİM  😎', 'https://t.me/slmBATU')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**📝 ETİKET KOMUTLARI **\n\n**» /utag < MESAJINIZ > \nGRUPTAKİ KULLANICILARI 5'Lİ ETİKET ATAR .  .  !**\n\n**» /tag  < MESAJINIZ > \nGRUPTAKİ KULLANICILARI TEK TEK ETİKET ATAR . . !**\n\n**» /cancel => ETİKETLEME İŞLEMİNİ DURDURUR . . !**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🎉  𝗕𝗼𝘁𝘂 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲  🎉', 'https://t.me/BugsBunyEtiket_bot?startgroup=a')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


emoji = " ❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 " \
        "😞 😔 😟 😕 🙁 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡  🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 " \
        "😻 😼 😽 🙀 😿 😾 🔞 🌹 ".split (" ")


@client.on(events.NewMessage(pattern="^/jssjejs ?(.*)"))
async def mentionall(event):
  global emoji_calisan
  if event.is_private:
    return await event.respond("**BU KOMUT GRUPLAR İÇİNDİR **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Komutu Sadece Yöneticiler Kullanabilir😐**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Geçmiş mesajlar için etiketetme yetkim yok**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Etiket yapmak için sebep yok**")
  else:
    return await event.respond("**Etikete başlamak için sebep yazmalısın...!**")
  
  if mode == "text_on_cmd":
    emoji_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("** Etiketleme işlemi durduruldu **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    emoji_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("**Etiketleme işlemi durduruldu ...**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**● Bu Komutu Yanlızca Grupta Kullanabilirsin . . !**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**● BU KOMUTU YANLIZCA YÖNETİCİLER KULLANABİLİR . . !**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajlara Cevab Vermeyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Etiket işlemini başlatmam için sebep yazmalısın**")
  else:
    return await event.respond("**● Etiket işlemini başlatmak için \n< SEBEP > Girin,Yada bir mesaja cevap verin . . !**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id})** , "
      if event.chat_id not in anlik_calisan:
        await event.respond("**● ETİKETLEME İŞLEMİ DURDURULDU . . !**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id})** , "
      if event.chat_id not in anlik_calisan:
        await event.respond("**● ETİKETLEME İŞLEMİ DURDURULDU . . !**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**● BU KOMUTU YANLIZCA GRUPTA KULLANABİLİRSİNİZ . . !**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**● BU KOMUTU YANLIZCA YÖNETİCİLER KULLANABİLİR . . !**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**önceki mesajı etiketleyemem*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**● Etiket işlemini başlatmak için \n< SEBEP > Girin,Yada bir mesaja cevap verin . . !**")
  else:
    return await event.respond("**● Etiket işlemini başlatmak için \n< SEBEP > Girin,Yada bir mesaja cevap verin . . !**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in tekli_calisan:
        await event.respond("**● Etiketleme İşi Durduruldu . . !**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} \n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**● Etiketleme İşi Durduruldu . . !**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/admin ?(.*)"))
async def mentionall(tagadmin):

	if admintag.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)


print(">> Bot Başlatıldı. Üyelere etiket atabilirim. <<")
client.run_until_disconnected()
