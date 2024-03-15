from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('hello')
    await context.bot.send_message(chat_id=update.effective_user.id, text='你好')
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    print(query.to_json())
    await query.edit_message_text(text=f"Selected option: {query.data}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('start')
    print(update.message.text)
    print(update.to_json())
    await context.bot.send_message(chat_id=update.effective_user.id, text='开始')
    await update.message.reply_text(f'开始 {update.effective_user.first_name}')


async def choujiang(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('choujiang')
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1", url='t.me/sz_wolf'),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def start1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Display a message with a button."""
    await update.message.reply_html(
        "This button was clicked <i>0</i> times.",
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton(text="Click me!", callback_data="start1")
        ),
    )


def run():
    print("run")
    app = ApplicationBuilder().token("6650155971:AAH7mL4QjBSDgpm1L1R28IZgKevn7l0aLOA").build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("start1", start1))
    app.add_handler(CommandHandler("choujiang", choujiang))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
