from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('hello')
    await context.bot.send_message(chat_id=update.effective_user.id, text='你好')
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')





def run():
    print("run")
    app = ApplicationBuilder().token("6650155971:AAH7mL4QjBSDgpm1L1R28IZgKevn7l0aLOA").build()

    app.add_handler(CommandHandler("hello", hello))

    app.run_polling()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
