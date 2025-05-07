
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

devices = {
    "noutbuklar": [
        {
            "nomi": "HP Pavilion 15",
            "narxi": "$919.99",
            "rasm": "https://nout.uz/wp-content/uploads/2023/02/86.png",
            "link": "https://www.hp.com/us-en/shop/pdp/hp-pavilion-laptop-15-eg3097nr"
        },
        {
            "nomi": "Dell XPS 13",
            "narxi": "$1599",
            "rasm": "https://m.media-amazon.com/images/I/61uCHVcsAvL._AC_SL1105_.jpg",
            "link": "https://www.dell.com/en-us/shop/dell-laptops/xps-13-laptop/spd/xps-13-9340-laptop"
        },
        {
            "nomi": "MacBook Air M2",
            "narxi": "$999",
            "rasm": "https://techcrunch.com/wp-content/uploads/2022/07/CMC_1580.jpg",
            "link": "https://www.apple.com/shop/buy-mac/macbook-air/13-inch-midnight-apple-m2-chip-with-8-core-cpu-and-8-core-gpu-16gb-memory-256gb"
        },
        {
            "nomi": "Lenovo ThinkPad X1 Carbon",
            "narxi": "$2267.10",
            "rasm": "https://p1-ofp.static.pub/medias/bWFzdGVyfHJvb3R8ODQ4NDd8aW1hZ2UvcG5nfGgyMi9oOGYvMTA2NzQ1ODc3Mjk5NTAucG5nfDQzODYxOTc5ODA0MWJhZTQyYThjOTAzZjE0NDI2NWVjYjY5MjE3MGFiMWEzODhlN2UyMGUwNGZhMWRmOTJmNzg/lenovo-laptop-thinkpad-x1-carbon-gen8-subseries-hero.png",
            "link": "https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpadx1/thinkpad-x1-carbon-gen-13-aura-edition-14-inch-intel/21ns0012us"
        }
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Noutbuklar", callback_data='noutbuklar')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Salom! Men Alyorbek tomonidan yaratilgan Telegram botman.
"
        "Men orqali kompyuter qurilmalarining onlayn savdosini amalga oshirishingiz mumkin.
"
        "Marhamat, kerakli bo'limni tanlang:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    category = query.data
    if category in devices:
        items = devices[category]
        for item in items:
            message = f"<b>{item['nomi']}</b>
💰 Narxi: {item['narxi']}
Quyida qurilmaning rasmi bilan tanishing."
            keyboard = [[InlineKeyboardButton("Sotib olish", url=item['link'])]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.message.reply_photo(
                photo=item['rasm'],
                caption=message,
                reply_markup=reply_markup,
                parse_mode='HTML'
            )

if __name__ == '__main__':
    TOKEN = "YOUR_BOT_TOKEN"
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    print("Bot ishga tushdi...")
    application.run_polling()
