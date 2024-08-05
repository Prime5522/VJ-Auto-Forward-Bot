from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "e6ea2eca4aa38e965511f323e5ffa578")
      API_ID = int(getenv("API_ID", "25425840"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7069060558:AAFtnTiG1V-86xCSCN7UYYK1S5GGOXYQsvI")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002110875043:-1002170173517").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
