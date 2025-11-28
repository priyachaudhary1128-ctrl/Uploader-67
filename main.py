from pyrogram import Client, filters
from helper.downloader import download_from_url
from helper.extractor import extract_zip
from helper.utils import safe_filename
from config import DRM_FOLDER, NON_DRM_FOLDER, CHANNEL_ID, OWNER_ID, API_ID, API_HASH, BOT_TOKEN
import os

bot = Client("UploaderBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply("Uploader Bot Active!")

@bot.on_message(filters.document)
async def file_handler(_, msg):
    file = msg.document
    name = safe_filename(file.file_name)
    path = (DRM_FOLDER if "drm" in name.lower() else NON_DRM_FOLDER) + name
    await msg.download(path)
    await bot.send_document(CHANNEL_ID, path, caption=name)
    await msg.reply(f"Uploaded {name}")

@bot.on_message(filters.text & ~filters.command)
async def url_handler(_, msg):
    url = msg.text
    if not url.startswith("http"):
        return
    file_path = await download_from_url(url)
    if file_path.endswith(".zip"):
        out = extract_zip(file_path)
        await msg.reply(f"Extracted: {out}")
    await bot.send_document(CHANNEL_ID, file_path)

bot.run()
