from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


class config :
	
	TOKEN = os.environ ["TOKEN"]
	API_ID = int (os.environ ["API_ID"])
	API_HASH = os.environ ["API_HASH"]



app = Client(
"Tasky",
api_id=config.API_ID,
api_hash=config.API_HASH,
bot_token=config.TOKEN)





@app.on_message(filters.command("start"))
async def start(client, message):
    name = message.from_user.first_name
    await message.reply_text(f'Hola {name}, puedo ayudarte a administrar tus grupos.',
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("🗯 Ayuda 🗯", callback_data="helpp")],
        [InlineKeyboardButton("➕ Agregarme al grupo ➕", url="http://t.me/Munkake_Bot?startgroup=start")

    ]]))
#comando callback de menu
@app.on_callback_query(filters.regex("menu"))
async def help(client, query):
    name = query.from_user.first_name
    await query.message.edit_text(f'Hola {name}, puedo ayudarte a administrar tus grupos.',
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("🗯 Ayuda 🗯", callback_data="helpp")],
        [InlineKeyboardButton("➕ Agregarme al grupo ➕", url="http://t.me/Munkake_Bot?startgroup=add")
    ]]))


# COMANDO CALLBACK DATA DE HELPP
@app.on_callback_query(filters.regex("helpp"))
async def help(client, query):
    name = query.from_user.first_name
    await query.message.edit_text(f'Hey {name}, aquí esta toda la información sobre mi',
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("⚙️ Comandos ⚙️", callback_data="commands")],
        [InlineKeyboardButton("❕Menú❕", callback_data="menu")
    ]]))

# COMANDO CALLBACK DATA DE COMMANDS
@app.on_callback_query(filters.regex("commands"))
async def commands(client, query):
    name = query.from_user.first_name
    await query.message.edit_text(f'❕La mayoría de los comandos solo son utilizables por administradores del chat.\n\n\n/pin - Responde a un mensaje con este comando en el chat para fijarlo\n\n/unpin - Responde a un mensaje fijado en el chat para desfijarlo\n\n/unpinall - Usar este comando en el chat desfija todos los mensajes fijados\n\n/ban - Responde al mensaje de un usuario en el chat para darle Ban\n\n/unban - responde al mensaje de un usuario baneado en el chat para retirarle el Ban\n\n/link - Muestra el enlace del chat',
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("❕Menú❕", callback_data="menu")
    ]]))














#      AVISOS
# Bienvenida nuevos miembos 
@app.on_message(filters.new_chat_members)
async def new_members(client, message):
    name = message.new_chat_members[0].first_name
    username = message.new_chat_members[0].username
    await message.reply(f"[{name}](https://t.me/{username}) ha entrado al chat", disable_web_page_preview=True)

# Aviso se fijo un mensaje
@app.on_message(filters.pinned_message)
async def new_photo(client, message):
    name = message.pinned_message.from_user.first_name
    username = message.pinned_message.from_user.username
    await message.reply(f"[{name}](https://t.me/{username}) fijo un mensaje ", disable_web_page_preview=True)
    
# Aviso se elimino la foto del chat 
@app.on_message(filters.delete_chat_photo)
async def new_photo(client, message):
    await message.reply(f"Se elimino la foto del chat ")




#             COMANDOS
# Comando pin
@app.on_message(filters.command("pin"))
async def pin(client, message):
    message_id = message.reply_to_message.message_id
    chat_id = message.reply_to_message.chat.id
    user_id = message.from_user.id
    member = await client.get_chat_member(chat_id, user_id)
    if member.status == "administrator":
        await client.pin_chat_message(chat_id, message_id)
        await message.reply(f"Se fijo el mensaje")
    elif member.status == "creator":
        await client.pin_chat_message(chat_id, message_id)
        await message.reply(f"Se fijo el mensaje")
    elif member.status == "is_anonymous":
        await client.pin_chat_message(chat_id, message_id)
        await message.reply(f"Se fijo el mensaje")
    else:
        await message.reply(f"No tienes permisos de admin")

# Comando unpin
@app.on_message(filters.command("unpin"))
async def unpin(client, message):
    message_id = message.reply_to_message.message_id
    chat_id = message.reply_to_message.chat.id
    user_id = message.from_user.id
    member = await client.get_chat_member(chat_id, user_id)
    if member.status == "administrator":
        await client.unpin_chat_message(chat_id, message_id)
        await message.reply(f"Se desfijo  el mensaje")
    elif member.status == "creator":
        await client.unpin_chat_message(chat_id, message_id)
        await message.reply(f"Se desfijo  el mensaje")
    elif member.status == "left":
        await client.unpin_chat_message(chat_id, message_id)
        await message.reply(f"Se desfijo  el mensaje")
    else:
        await message.reply(f"No tienes permisos de admin")

# Comando unpinall
@app.on_message(filters.command("unpinall"))
async def unpinall(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    member = await client.get_chat_member(chat_id, user_id)
    if member.status == "administrator":
        await client.unpin_all_chat_messages(chat_id)
        await message.reply(f"Se desfijaron todos los mensajes")
    elif member.status == "creator":
        await client.unpin_all_chat_messages(chat_id)
        await message.reply(f"Se desfijaron todos los mensajes")
    elif member.status == "left":
        await client.unpin_all_chat_messages(chat_id)
        await message.reply(f"Se desfijaron todos los mensajes")
    else:
        await message.reply(f"No tienes permisos de admin")



# comando ban
@app.on_message(filters.command("ban"))
async def ban(client, message):
    chat_id = message.reply_to_message.chat.id
    user_id_ban = message.reply_to_message.from_user.id
    user_id = message.from_user.id
    username = message.reply_to_message.from_user.username
    name = message.reply_to_message.from_user.first_name
    member = await client.get_chat_member(chat_id, user_id)
    if member.status == "administrator":
        await client.kick_chat_member(chat_id, user_id_ban)
        await message.reply(f"Se le aplico un Ban al usuario [{name}](https://t.me/{username})", disable_web_page_preview=True)
    elif member.status == "creator":
        await client.kick_chat_member(chat_id, user_id_ban)
        await message.reply(f"Se le aplico un Ban al usuario [{name}](https://t.me/{username})", disable_web_page_preview=True)
    elif member.status == "is_anonymous":
        await client.kick_chat_member(chat_id, user_id_ban)
        await message.reply(f"Se le aplico un Ban al usuario [{name}](https://t.me/{username})", disable_web_page_preview=True)
    else:
        await message.reply(f"No tienes permisos de admin")

# comando unban
@app.on_message(filters.command("unban"))
async def unban(client, message):
    chat_id = message.reply_to_message.chat.id
    user_id_ban = message.reply_to_message.from_user.id
    user_id = message.from_user.id
    username = message.reply_to_message.from_user.username
    name = message.reply_to_message.from_user.first_name
    member = await client.get_chat_member(chat_id, user_id)
    if member.status == "administrator":
        await client.unban_chat_member(chat_id, user_id_ban)
        await message.reply(f"Se le retiro el Ban al usuario [{name}](https://t.me/{username})", disable_web_page_preview=True)
    elif member.status == "creator":
        await client.unban_chat_member(chat_id, user_id_ban)
        await message.reply(f"Se le retiro el Ban al usuario [{name}](https://t.me/{username})", disable_web_page_preview=True)
    elif member.status == "is_anonymous":
        await client.unban_chat_member(chat_id, user_id_ban)
        await message.reply(f"Se le retiro el Ban al usuario [{name}](https://t.me/{username})", disable_web_page_preview=True)
    else:
        await message.reply(f"No tienes permisos de admin")


# comando link 
@app.on_message(filters.command("link"))
async def link(client, message):    
    chat_id = message.chat.id
    user_id = message.from_user.id
    member = await client.get_chat_member(chat_id, user_id)
    if member.status == "administrator":
        await message.reply(f"https://t.me/{message.chat.username}")
    elif member.status == "creator":
        await message.reply(f"https://t.me/{message.chat.username}")
    elif member.status == "is_anonymous":
        await message.reply(f"https://t.me/{message.chat.username}")
    else:
        await message.reply(f"No tienes permisos de admin")













print('Bot Online')
app.run()
