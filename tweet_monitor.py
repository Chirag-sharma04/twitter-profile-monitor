import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium WebDriver with logged-in Chrome session
def setup_driver():
    print("Setting up Chrome driver...")
    chrome_options = Options()
    chrome_options.add_argument(r'--user-data-dir=C:\Users\LENOVO\AppData\Local\Google\Chrome\User Data')
    chrome_options.add_argument(r'--profile-directory=Profile 1')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Monitor new posts from the target Twitter page
def monitor_twitter_page():
    driver = setup_driver()
    url = "https://x.com/DearS_o_n"
    driver.get(url)
    time.sleep(5)  # Allow page to load
    
    seen_posts = set()
    
    try:
        while True:
            driver.refresh()
            time.sleep(5)  # Allow refreshed content to load
            
            tweets = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
            
            for tweet in tweets:
                tweet_text = tweet.text.strip()
                if tweet_text and tweet_text not in seen_posts:
                    seen_posts.add(tweet_text)
                    print(f"New Post: {tweet_text}\n")
            
            time.sleep(10)  # Wait before refreshing again
    except KeyboardInterrupt:
        print("Stopping monitoring...")
    finally:
        driver.quit()

if __name__ == "__main__":
    monitor_twitter_page()
