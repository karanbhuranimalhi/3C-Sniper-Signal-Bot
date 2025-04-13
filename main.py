import os
import telebot
import time

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
channel_username = "@tradelikeapropublic"

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Sniper 3C Bot Activated!")

def send_signal():
    signal = "EUR/USD 1M Buy Confirmed - Sniper Signal"
    bot.send_message(channel_username, signal)

if __name__ == "__main__":
    while True:
        send_signal()
        time.sleep(300)
