import re
from os import environ
from Script import script

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Error - {type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '18952416')
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', '31e9fc0bb79e50d63092895ef64b991e')
if len(API_HASH) == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '5481546790:AAFavWFUN59MO7tp2QSri7scMOLDV5BSiLw')
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '8080'))

# Bot pics
PICS = (environ.get('PICS', 'https://telegra.ph/file/6d83965497670b153349c.jpg https://telegra.ph/file/48ab47e0347574da9b40e.jpg https://telegra.ph/file/0348681d8f3dd5b0d0c99.jpg https://telegra.ph/file/961b83193edf1fd86358d.jpg https://telegra.ph/file/752fce12f691a2e6604e0.jpg https://telegra.ph/file/aaf292ad7bc6d97a3859b.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '5533079371 5207138613')
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1002043045800 -1001866646571').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1001766555154')
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)

# support group
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1001732232755')
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://darkdevilmp:darkdevil007mp@autofilterddmp.zuw3c4q.mongodb.net/?retryWrites=true&w=majority")
if len(DATABASE_URL) == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "Autofilterddmp")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/+EapqivvgHbc5YmY1')
OWNER_USERNAME = environ.get("OWNER_USERNAME", "https://t.me/mpbotzsupport_bot")
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/infinity_botzz')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/+nF7KliSj3RFkMzY1')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/links_tutorialbypp/23")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/links_tutorialbypp/23")

# Bot settings
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'bengali hindi english telugu tamil kannada malayalam marathi punjabi gujarati').split()]
QUALITY = [quality.lower() for quality in environ.get('QUALITY', 'Hdrip Web-Dl Bluray HDR FHD 240P 480P 540P 720P 1080P 1440P 2K 2160P 4K').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "tnshort.net")
SHORTLINK_API = environ.get("SHORTLINK_API", "b2da06188bd355e103d16ab1b56db314709740df")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
PM_FILE_DELETE_TIME = int(environ.get('PM_FILE_DELETE_TIME', '3600'))

# boolean settings
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
IS_VERIFY = is_enabled('IS_VERIFY', True)
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
WELCOME = is_enabled('WELCOME', True)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', False)

#premium info
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/f21404a4882698d5488dd.jpg')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'paradox52693@okhdfcbank')

# for stream
IS_STREAM = is_enabled('IS_STREAM', True)
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1001964309084")
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "https://eventual-catlaina-infinity-movies-bot-mp-b67bd5a1.koyeb.app/") #https://infinity-movies-bot-07.onrender.com/
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()

#start_command_reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"] #don't add any emoji because tg not support all emoji reactions
