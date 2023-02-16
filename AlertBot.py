import telegram
import asyncio
import re
import urllib.parse

async def send_signal(trading_pair, signal_type):
    bot_token = "6119983782:AAGwSeqDU2E7UfyhIz6t2wh81AGopsMjZx8"
    bot = telegram.Bot(token=bot_token)
    channel_name = "@SignalBot100"
    await bot.send_message(chat_id=channel_name, text=trading_pair + " " + signal_type)

async def main(trading_view_message):
    message = urllib.parse.unquote(trading_view_message) # decode message
    regex = r"(.+):(.+)\n(.+) @ efectuada en (.+)\nMomento de (.+)\n(.+) en (.+)" # regular expression to parse message
    matches = re.match(regex, message, re.MULTILINE | re.DOTALL)
    if matches:
        exchange = matches.group(1)
        ticker = matches.group(2)
        action = matches.group(3)
        price = matches.group(4)
        order_type = matches.group(5)
        time = matches.group(6)
        interval = matches.group(7)
        signal_type = f"{action} {order_type} at {price} on {time} {interval}"
        trading_pair = f"{exchange}:{ticker}"
        await send_signal(trading_pair, signal_type)
    else:
        print("Could not parse message.")

if __name__ == "__main__":
    trading_view_message = input("Enter the TradingView message: ")
    asyncio.run(main(trading_view_message))
