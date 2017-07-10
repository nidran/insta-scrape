from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

def login(driver):
   
    # Load page
    driver.implicitly_wait(random.randrange(20,40))
    driver.get("https://www.instagram.com/accounts/login/")
    driver.implicitly_wait(random.randrange(20,70))

    # Login
    username = "nidhiiranjan"  # <username here>
    password = "Nid1451996!"  # <password here>
    driver.find_element_by_xpath("//div/input[@name='username']").send_keys(username)
    driver.implicitly_wait(random.randrange(10,15))
    driver.find_element_by_xpath("//div/input[@name='password']").send_keys(password)
    driver.implicitly_wait(random.randrange(10,15))
    driver.find_element_by_xpath("//span/button").click()
    print "Logged In"
    # Wait for the login page to load
    # WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.LINK_TEXT, "See All")))


def scrape_followers(driver, account):
    # Load account page
    driver.implicitly_wait(random.randrange(40,70))
    driver.get("https://www.instagram.com/{0}/".format(account))
    driver.implicitly_wait(random.randrange(70,90))
    print "Opened instagram"
    # Click the 'Follower(s)' link
    driver.find_element_by_partial_link_text("follower").click()

    # Wait for the followers modal to load
    xpath = "//div[@style='position: relative; z-index: 1;']/div/div[2]/div/div[1]"
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    print "Follower section ..."

    # You'll need to figure out some scrolling magic here. Something that can
    # scroll to the bottom of the followers modal, and know when its reached
    # the bottom. This is pretty impractical for people with a lot of followers

    # Finally, scrape the followers
    print "Starting to scrape followers ..."
    xpath = "//div[@style='position: relative; z-index: 1;']//ul/li/div/div/div/div/a"
    followers_elems = driver.find_elements_by_xpath(xpath)
    print "Executing followers ..."
    return [e.text for e in followers_elems]


if __name__ == "__main__":
    driver = webdriver.Firefox()
    try:
        login(driver)
        followers = scrape_followers(driver, "instagram")
        # print(followers)
    finally:
        driver.quit()