# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "9972455"))
API_HASH = getenv("API_HASH", "5b1fd83b698e4e6670f3dcb053eecc06")
BOT_TOKEN = getenv("BOT_TOKEN", "7430047499:AAF5Et-Y2Zm1lAAp9hVM-_T3X8u0Vu5XslA")
OWNER_ID = int(getenv("OWNER_ID", "6928637808"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://mainmusicbot:musicbotdatabase@cluster0.hbvhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002357764876"))
FORCESUB = getenv("FORCESUB", "-1002391820880")
