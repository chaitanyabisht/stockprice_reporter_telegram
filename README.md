# stockprice_reporter_telegram
stockprice_reporter_telegram function at AWS Lambda

there are two environment variables set up: CHAT_ID and TELEGRAM_TOKEN


This program checks the stock price from yahoo finance every 4 hours.
If the stock price goes below or above the given minprice and maxprice attribute, a telegram bot (mpccinfo_bot) notifies
