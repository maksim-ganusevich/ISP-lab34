import os


BOT_TOKEN = os.getenv("BOT_TOKEN", "2013117162:AAEVvsH6A5EEyO-v-kCXctidyNiWBPljlII")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://0656-46-216-181-36.eu.ngrok.io") #front 5001
URL_WEB = os.getenv("URL_WEB", "https://0453-46-216-181-36.eu.ngrok.io") #back 5000
TELEGRAM_URL = "https://api.telegram.org"
DATA = {"url": WEBHOOK_URL}
SET_WEBHOOK_URL = f"{TELEGRAM_URL}/bot{BOT_TOKEN}/setWebhook"
BOT_URL = f"{TELEGRAM_URL}/bot{BOT_TOKEN}/"
