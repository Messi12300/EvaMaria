import os
import requests
import random
from Script import script
from info import DICE
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


API = "https://api.sumanjay.cf/covid/?country="



@Client.on_message(filters.command(['corona']))
async def corona(client, message):
    await message.reply_text(
        text=covid_info(client, message),
        quote=True
    )


def covid_info(client, message):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**Covid 19 Information**--
Country : `{country}`
Actived : `{active}`
Confirmed : `{confirmed}`
Deaths : `{deaths}`
ID : `{info_id}`
Last Update : `{last_update}`
Latitude : `{latitude}`
Longitude : `{longitude}`
Recovered : `{recovered}`
Made with ❣️ by @MC_Group1"""
        return covid_info
    except Exception as error:
        return
