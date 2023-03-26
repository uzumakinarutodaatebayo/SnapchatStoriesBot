import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "14157322"))
    API_HASH = os.environ.get("API_HASH", "9271a3e8d68ea664d83964953b8de084")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6047099925:AAHSD6HnuwoUA_l7FlSGHUQx_zitMjBDvh8")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "movies_zilla_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
