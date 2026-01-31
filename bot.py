from telegram.ext import Application, CommandHandler, MessageHandler, filters
from openai import OpenAI
import os

# 🔐 TOKENLAR ENV ORQALI
BOT_TOKEN = os.getenv("8265650695:AAFPencp8AO_09IeA0kSsO3E8-q69WYTqEk")
OPENAI_API_KEY = os.getenv("sk-abc123xyz456.....")

client = OpenAI(api_key=OPENAI_API_KEY)

async def start(update, context):
    await update.message.reply_text(
        "Salom 👋\nSavolingni yoz — AI javob beradi 🤖"
    )

async def chat(update, context):
    user_text = update.message.text

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_text}
            ]
        )

        answer = response.choices[0].message.content
        await update.message.reply_text(answer)

    except Exception as e:
        await update.message.reply_text("Xatolik yuz berdi 😕")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    app.run_polling()

if __name__ == "__main__":
    main()
