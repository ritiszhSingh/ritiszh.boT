from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "")
BOT_TOKEN = getenv("BOT_TOKEN", "5017437484:AAFMfMn38ZbipZaJbePQJu4nM4cju-VZQeo")
API_ID = int(getenv("API_ID", "18169998"))
API_HASH = getenv("API_HASH", "450a7dc545e3baa93961524c595714f5")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "70"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://music:music@cluster0.cpkaz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5013661292").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5013661292").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001457893155"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐑𝐢𝐓𝐢𝐒𝐳𝐡 𝐁𝐎𝐓")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/9b74d0c1c95e5ed6124fa.jpg")
if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))
