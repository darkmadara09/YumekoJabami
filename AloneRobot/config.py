class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "13279715" # integer value, dont use ""
    API_HASH = "56e198053932ecf216af72a2ddffcd78"
    TOKEN = "6413944722:AAENoBygE8dP7VAxYpyFSzMDKgoaNn00VHo"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 7122227582 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "Love_And_War_Bby"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph/file/5ef552704f37386e53ddb.jpg"
    EVENT_LOGS = (-1002069450766)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://bikash:bikash@bikash.3jkvhp7.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://dwhesbut:l0W9zw6yDi38CuwbOrI3ztJJ3FdjEnAH@flora.db.elephantsql.com/dwhesbut"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    CHATBOT_API="" # get it from @FallenChat_Bot using /token
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
