# kyancer_bot

## Summary
Telegram bot that turns plain text into headaches. Can be found at https://t.me/kyancer_bot

## How to use
The bot uses inline messages. It can be used in other chats by typing `@kyancer_bot <mytexthere>` in aforementioned other chats. There's probably more elegant ways to program it but this was a quick project where I wasn't too concerned about speed or optimality. 

* `pip install python-telegram-bot --upgrade` in terminal
* [Get](https://core.telegram.org/bots#botfather-commands) a telegram bot API key
* Enable inline mode (see previous link)
* Add the API key as an environment variable
* Restart (or add API key into the file if restarting is too much commitment for you)
* `python kyancer_bot.py` in terminal when you're in the directory with the file
* `/start` to the [bot](https://t.me/kyancer_bot)
* `@mybotname_bot <mytexthere>` to your poor, poor friends on telegram

## Todo
* Replace ngrams instead of single characters
* Use regex engine instead of string replacement engine
* Actually turn this into something useful