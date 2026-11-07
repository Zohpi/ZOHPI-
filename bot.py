import telebot

# التوكن مكتوب صح بين علامات تنصيص
TOKEN = "9123231669:AAFl7SSmhvxKUL3NVqIwO8fYLy-7PIwNdl8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.text.strip() == 'ثانوي')
def send_link(message):
    # حط الرابط بتاعك هنا
    my_link = "https://example.com/secondary-link"
    bot.reply_to(message, f"اتفضل الرابط:\n{my_link}")

@bot.message_handler(func=lambda message: True)
def handle_others(message):
    bot.reply_to(message, "أهلاً بيك! ابعت كلمة 'ثانوي' عشان تاخد الرابط.")

print("البوت يعمل الآن...")
bot.polling()
