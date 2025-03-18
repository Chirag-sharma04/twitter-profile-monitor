Twitter Post Monitoring Bot
This Python script uses Selenium to monitor new posts on a specific Twitter (X) page. It continuously checks for new tweets, extracts their text, and prints them in real-time.

Features
Uses a logged-in Chrome session for seamless access.
Automatically refreshes the Twitter page to detect new tweets.
Extracts and prints newly posted tweets in real-time.
Runs continuously until interrupted by the user (Ctrl + C).
Prerequisites
Python 3.x
Google Chrome installed
Selenium installed (pip install selenium webdriver-manager)
WebDriver Manager for Chrome (pip install webdriver-manager)
A logged-in Chrome session with the correct profile path.
Setup Instructions
Ensure you are logged into Twitter (X) using Google Chrome.
Find your Chrome profile path:
Open Chrome and go to chrome://version/.
Locate Profile Path, e.g., C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Profile 1.
Update the profile path in setup_driver() function:
python
Copy
Edit
chrome_options.add_argument(r'--user-data-dir=C:\Users\YourName\AppData\Local\Google\Chrome\User Data')
chrome_options.add_argument(r'--profile-directory=Profile 1')
Run the script:
bash
Copy
Edit
python script.py
The script will monitor the specified Twitter page and display new posts.
Stopping the Script
Press Ctrl + C in the terminal to stop monitoring.

Notes
This script relies on Selenium and Chrome WebDriver, so ensure they are installed.
Running the script too frequently may lead to rate limiting or bans from Twitter (X).
Modify the time.sleep() intervals in monitor_twitter_page() if necessary to balance speed and stability.
