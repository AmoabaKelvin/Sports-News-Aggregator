import os

from dotenv import load_dotenv
from telebot import TeleBot

from main import fetch

load_dotenv()

bot = TeleBot(os.getenv("TELEGRAM_TOKEN"))


def get_and_send_updates():
    """
    This function calls the fetch function and saves the news to a file.
    The file is then sent to the user and deleted after being sent.
    """
    all_stories = ""
    stories, links = fetch()
    for story, link in zip(stories, links):
        all_stories += f"{story}\n{link}\n\n\n"
    with open("stories.txt", "w") as f:
        f.write(all_stories)
        bot.send_document(
            chat_id=os.getenv("CHAT_ID"), document=open("stories.txt", "rb")
        )
    os.remove("stories.txt")


@bot.message_handler(commands=["start"])
def start(message):
    """
    Send a welcome message to the user
    """
    bot.reply_to(message, "Hi, Congrats for joining!")


@bot.message_handler(commands=["newsnow"])
def send_news(message):
    """
    Get the latest news from the source and send to the user
    """
    get_and_send_updates()


if __name__ == "__main__":
    bot.polling()
