# Twitter Post Monitor

This Python script uses Selenium to monitor a specific Twitter (X) page and notify you of new posts. It continuously refreshes the page and checks for new tweets, printing the text of any new posts to the console.

## Prerequisites

* Python 3.x
* Chrome browser installed
* Selenium library (`pip install selenium`)
* webdriver-manager (`pip install webdriver-manager`)

## Setup

1.  **Install Dependencies:**

    ```bash
    pip install selenium webdriver-manager
    ```

2.  **Chrome User Data Directory:**
    * The script uses a specific Chrome user data directory (`C:\Users\LENOVO\AppData\Local\Google\Chrome\User Data`) and profile (`Profile 1`).
    * **Important:** You need to replace this path with the actual path to your Chrome user data directory and profile. This allows the script to use your logged-in Chrome session.
    * To find your Chrome user data directory:
        * Open Chrome.
        * Go to `chrome://version/`.
        * Look for "Profile Path". The parent directory of this path is your user data directory.
        * To find your profile name, examine the folder names under the user data directory.
3.  **Target Twitter Page:**
    * The script monitors the Twitter page `https://x.com/DearS_o_n`. You can change this URL in the `monitor_twitter_page()` function to monitor a different page.

## Usage

1.  **Run the Script:**

    ```bash
    python your_script_name.py
    ```

2.  **Monitoring:**
    * The script will open a Chrome browser window and navigate to the specified Twitter page.
    * It will continuously refresh the page and check for new tweets.
    * Any new tweets will be printed to the console.
    * The script will continue running until you press `Ctrl+C` to stop it.

## Code Explanation

* **`setup_driver()`:**
    * Initializes the Selenium WebDriver with Chrome options, including the user data directory and profile.
    * Uses `webdriver_manager` to automatically download the correct ChromeDriver.
* **`monitor_twitter_page()`:**
    * Sets up the WebDriver and navigates to the target Twitter page.
    * Uses a `while True` loop to continuously monitor the page.
    * Refreshes the page and waits for it to load.
    * Finds all tweet text elements using an XPath selector.
    * Checks for new tweets by comparing the tweet text to a set of seen posts.
    * Prints new tweets to the console.
    * Waits for a specified interval before refreshing again.
    * Handles `KeyboardInterrupt` to gracefully stop the script.

## Notes

* This script relies on the HTML structure of the Twitter page. If Twitter changes its HTML, the script may need to be updated.
* The refresh interval and wait times can be adjusted in the `monitor_twitter_page()` function.
* Make sure that your Chrome user data directory and profile are correctly specified.
* This script is basic and does not handle advanced features like notifications or error handling.
* Due to changes to X.com, this script may need to have the xpath updated frequently.
