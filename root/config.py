import os 

class Config(object):
  APP_ID = int(os.environ.get("APP_ID", "14082290"))
  API_HASH = os.environ.get("API_HASH", "ef7c8ee7f5a019ccca3f28d441d3bc49")
  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7417445493:AAFgeihC8i_f0V0MdMd8boMH8mhV3gmqHHw")
  AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
  DOWNLOAD_LOCATION = "./bot/DOWNLOADS"
  DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Vcam:Vcam@cluster0.ntboh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
  # owner is for log cmd only owner can use (this can be multiple users)
  OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "1735097089").split(" ")]
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Chayan223")
  CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION",False)
