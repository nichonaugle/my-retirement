import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Get Discord Webhook from environment variable 
# sorry bro, not gonna hardcode my credentials
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# TradingView chart URL
TRADINGVIEW_URL_FOR_TQQQ_QQQ = "https://www.tradingview.com/script/wKgbd52f-TICKER-COMPARE-QQQ-TQQQ/"

# Set up Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920x1080")

def get_tradingview_data():
    """Extracts SMA (Simple Moving Average) and closing price from TradingView."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(TRADINGVIEW_URL_FOR_TQQQ_QQQ)
    time.sleep(5)  # Wait for the page to load

    try:
        # Extract SMA value
        sma_element = driver.find_element(By.XPATH, "//div[@title='Moving Average of Comparative Ticker']")
        sma_value = sma_element.text

        # Extract Closing Price
        close_element = driver.find_element(By.XPATH, "//div[@title='Comparative Ticker Price']")
        closing_price = close_element.text

        driver.quit()
        return {"sma": sma_value, "closing_price": closing_price}

    except Exception as e:
        driver.quit()
        return {"error": str(e)}

def send_discord_notification():
    """Sends a Discord message with the extracted TradingView data."""
    data = get_tradingview_data()
    if "error" in data:
        message = f"❌ Error fetching data: {data['error']}"
    else:
        position_state = "Open ✔️" if float(data["closing_price"]) > float(data["sma"]) else "Closed ❌"
        message = (
            f"📈 **Daily Trading Update**\n"
            f"🔹 **SMA (Close):** {data['sma']}\n"
            f"💰 **Closing Price:** {data['closing_price']}\n"
            f"📅 **Date:** {time.strftime('%Y-%m-%d')}\n"
            f"🕒 **Time:** {time.strftime('%H:%M:%S')}\n"
            f"📊 **Ticker:** TQQQ\n"
            f"📊 **Position:** {position_state}\n"
        )

    requests.post(DISCORD_WEBHOOK_URL, json={"content": message})

# Run the function
if __name__ == "__main__":
    send_discord_notification()
