import os
import yfinance as yf
import pandas as pd
import requests
import time
from datetime import date

# Get Discord Webhook from environment variable
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def calculate_sma(ticker, sma_period=185):
    """
    Downloads daily close prices from yfinance (last year) and calculates the SMA,
    ensuring it uses the close of the current date. Raises an exception if today's data is missing.

    Args:
        ticker (str): The stock ticker symbol (e.g., "QQQ").
        sma_period (int): The period for the Simple Moving Average.
    """
    try:
        # Download daily historical data (last year)
        data = yf.download(ticker, period="1y")
        if data.empty:
            print(f"No data found for ticker: {ticker}")
            return None

        # Ensure the data contains the current date's close
        today = date.today()
        today_str = today.strftime('%Y-%m-%d')
        if today_str not in data.index.strftime('%Y-%m-%d'):
            raise ValueError(f"Data for today ({today_str}) not available.")

        # Calculate the SMA
        data['SMA'] = data['Close'].rolling(window=sma_period).mean()

        # Get the close price for the current date
        last_close = data.loc[today_str, 'Close']

        # Get the last SMA value
        last_sma = data['SMA'].iloc[-1]

        return {"sma": last_sma, "closing_price": last_close}

    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}

def send_discord_notification():
    """Sends a Discord message with the extracted yfinance data."""
    tqqq_signal = calculate_sma("QQQ")
    if "error" in tqqq_signal or tqqq_signal is None:
        message = f"❌ Error fetching data: {tqqq_signal['error'] if tqqq_signal else 'Data fetch failed'}"
    else:
        # Extract the float from the Series using .iloc[0]
        closing_price = float(tqqq_signal["closing_price"].iloc[0])
        position_state = "Open TQQQ Position✔️" if closing_price > float(tqqq_signal["sma"]) else "Close TQQQ Position❌"
        message = (
            f"📈 **Daily Trading Update**\n"
            f"🔹 **SMA (185):** {tqqq_signal['sma']:.2f}\n"
            f"💰 **Closing Price:** {closing_price:.2f}\n"
            f"📅 **Date:** {time.strftime('%Y-%m-%d')}\n"
            f"🕒 **Time:** {time.strftime('%H:%M:%S')}\n"
            f"📊 **Ticker:** QQQ\n"
            f"📊 **Position:** {position_state}\n"
        )

    print(message)
    if DISCORD_WEBHOOK_URL:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
    else:
        print("Discord Webhook URL not set. Cannot send notification.")

# Run the function
if __name__ == "__main__":
    send_discord_notification()