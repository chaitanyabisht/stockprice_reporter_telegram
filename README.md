# stockprice_reporter_telegram
stockprice_reporter_telegram function at AWS Lambda

This checks for stock price(stock names are provided in the code) from yahoo finance every 4 hours and checks if the stock price is below or above the given parameters.
If it falls below a certain price or rises above certain price it messages it into a telegram channel

there are two environment variables set up: CHAT_ID and TELEGRAM_TOKEN
