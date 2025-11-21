import re, os, time


class Config(object):

    # Regex Pattern
    id_pattern = re.compile(r'^-?\d+$')

    # Basic Bot Configuration
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Database
    DB_NAME = os.environ.get("DB_NAME", "AutoRenameBot")
    DB_URL  = os.environ.get("DB_URL", "")
    PORT    = os.environ.get("PORT", "8080")

    # Admin & Channel settings
    ADMIN = [int(x) for x in os.environ.get("ADMIN", "").split() if id_pattern.search(x)]

    FORCE_SUB_CHANNELS = os.environ.get("FORCE_SUB_CHANNELS", "0").split(',')

    LOG_CHANNEL  = int(os.environ.get("LOG_CHANNEL")) if os.environ.get("LOG_CHANNEL") else None
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL")) if os.environ.get("DUMP_CHANNEL") else None

    # Other Config
    BOT_UPTIME = time.time()
    START_PIC  = os.environ.get("START_PIC", "https://graph.org/file/29a3acbbab9de5f45a5fe.jpg")

    WEBHOOK = os.environ.get("WEBHOOK", "True").lower() == "true"



class Txt(object):

    START_TXT = """Hello {},

I am an Auto Rename Bot.
I can rename files automatically, set custom captions & thumbnails,
and support episode-based auto formatting.

Send any file to begin.
"""

    FILE_NAME_TXT = """Auto Rename Format Setup

Variables:
• episode – Episode number
• season – Season number
• quality – Video quality

Example:
/autorename Overflow [Sseason Eepisode] quality
"""

    FORMAT_VARIABLES = """
<b>VARIABLES:</b>
• episode – Replace episode number
• season – Replace season number
• quality – Replace video quality

<b>Example:</b> `/autorename Overflow [Sseason Eepisode] - [Dual] quality`
"""

    THUMBNAIL_TXT = """Custom Thumbnail Setup:

• Send a photo to set thumbnail
• /view_thumb – View current thumbnail
• /del_thumb – Delete thumbnail
"""

    CAPTION_TXT = """Custom Caption Format

Available variables:
{filename} – file name
{filesize} – size
{duration} – duration

Commands:
/set_caption – Set caption
/see_caption – View caption
/del_caption – Delete caption
"""

    PROGRESS_BAR = """
Progress:
Completed: {0}%
Size: {1} / {2}
Speed: {3}/s
ETA: {4}
"""

    HELP_TXT = """Help Menu

• /autorename – Auto rename media
• /metadata – Enable/Disable metadata editing
• /help – Show help menu
"""

    SEND_METADATA = """
Metadata Settings

/metadata – Toggle metadata update for MKV files
"""

    ABOUT_TXT = f"""<b>❍ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/codeflix_bots">ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ</a>
❍ ᴅᴇᴠᴇʟᴏᴩᴇʀ : <a href="https://t.me/cosmic_freak">ʏᴀᴛᴏ</a>
❍ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>
❍ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
❍ ʜᴏꜱᴛᴇᴅ ᴏɴ : ᴠᴘs
❍ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/animes_cruise">ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a></b>
"""

    PREMIUM_TXT = """Premium Plan

• Unlimited renaming
• Early access features

Use /plan to view premium plans
"""

    PREPLANS_TXT = """Available Premium Plans

• Monthly: ₹50
• Daily: ₹5

UPI: <code>LodaLassan@fam</code>
"""

    META_TXT = """
Metadata control for videos

/settitle
/setauthor
/setartist
/setaudio
/setsubtitle
/setvideo
"""
