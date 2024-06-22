import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
# Set up the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()

def create_database():
    # Save the data to an SQLite database
    conn = sqlite3.connect('test_results.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS results (first_name TEXT)''')
    conn.commit()
    conn.close()


def run_selenium_script():
    # Set up the WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome()
    # Open the web page with the form
    driver.get('https://forms.gle/ua1ZsyuxWUxUU9Ts5')
    first_name_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    last_name_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    email_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    submit_btn_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'

    # Locate form elements and fill them in
    driver.find_element(By.XPATH, first_name_xpath).send_keys('Amirul')
    driver.find_element(By.XPATH, last_name_xpath).send_keys('Hakim')
    driver.find_element(By.XPATH, email_xpath).send_keys('Amirul.hakim@example.com')
    # Submit the form
    driver.find_element(By.XPATH, submit_btn_xpath).click()

    #evidence
    driver.save_screenshot('screenshot.png')


# Run the steps
create_database()
run_selenium_script()


# Close the browser
driver.quit()



