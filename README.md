# stockprice_reporter_telegram
stockprice_reporter_telegram function at AWS Lambda

There are two environment variables set up: CHAT_ID and TELEGRAM_TOKEN


This program checks the stock price from Yahoo Finance every t minutes.
If the stock price goes below or above the given minprice and maxprice attribute, a bot on telegram will message you.
