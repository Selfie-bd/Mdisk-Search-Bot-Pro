# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 1976680))
    API_HASH = os.getenv("API_HASH", "9073255ce64a6072a59099803493f97d")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5629666099:AAHs-AmJwGfqtKLj_dPCMYZXD0qddSu-Jkk")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "EpicMovieSearchBot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -1001821753399))
    BOT_USERNAME = os.getenv("BOT_USERNAME","EpicMovieSearchBot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", 5657684746))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Balaepic")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME", "epic_flims")
    START_MSG = os.getenv("START_MSG")
    START_PHOTO = os.getenv("START_PHOTO")
    HOME_TEXT = os.getenv("HOME_TEXT")
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", -1001821753399)
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", ""-1001859746470))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "False")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "epicflims")
    FORCE_SUB = os.getenv("FORCE_SUB", "True")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "12334")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "1"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT")
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT")
