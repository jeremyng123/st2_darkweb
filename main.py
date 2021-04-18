# from soup_scrape import *
import csv
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from load_data import *
from scrape import *
from urls import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

fieldnames = [
    "vendor", "about", "listings", "reviews", "ratings", "number of profiles",
    "profiles (site: link)"
]


def searchWithKilo():
    # print(f'\n\n\n{os.path.dirname(os.path.abspath(__file__))} \n\n\n')
    file = open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                     "kilo_scrape.csv"), "w")
    try:
        csv_file = csv.writer(file, delimiter=',')
        for index, vendor in enumerate(vendors):
            try:
                # get to main profile page
                driver.get(KILOS_VENDOR.format(vendor))
                about = driver.find_element_by_xpath(
                    ".//textarea").get_attribute('value')
                # print(f"\n\nabout:\n{about.get_attribute('value')}")
                stats = driver.find_elements_by_class_name("stat")
                numLists = stats[0].text
                numReviews = stats[1].text
                avgRating = stats[2].text
                numProfiles = stats[3].text
                # get to market profiles
                driver.get(KILOS_MARKET_PROFILE.format(vendor))
                table = driver.find_element_by_xpath("//tbody")
                sites = set()
                links = {}
                market_profiles = ""
                for i, row in enumerate(table.find_elements_by_xpath(".//tr")):
                    if i == 0:  # table header
                        continue
                    tds = row.find_elements_by_xpath(".//td")
                    sites.add(tds[0].text)
                    if tds[0].text not in links.keys() or links[
                            tds[0].
                            text] == "http://dead.site.dont.visit.onion/removed_for_user_safety":
                        links[tds[0].text] = tds[1].text

                for site, link in links.items():
                    market_profiles += f"{site}: {link}\n"
                csv_file.writerow([
                    vendor, about, numLists, numReviews, avgRating,
                    numProfiles, market_profiles[:-1]
                ])
                file.flush()

                print(
                    f"{index}: {vendor, about, numLists, numReviews, avgRating, numProfiles, market_profiles[:-1]}"
                )
            except NoSuchElementException:
                continue
    except KeyboardInterrupt:
        print("\n\nKeyboardInterrupt!!!!!!\n\n\n")
        file.flush()
        file.close()
    finally:
        file.close()


def searchWithRecon():
    for vendor in vendors:
        driver.get(RECON1 + "/vendor")
        searchbox = driver.find_element_by_name("vendor_username")
        searchbox.send_keys(vendor)
        searchbox.send_keys(Keys.ENTER)
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'market-name')]")))
            vendor_page = driver.current_url
            profiles = driver.find_elements_by_xpath(
                "//div[contains(@class, 'market-name')]")
            for profile in profiles:
                print(profile.text)

        except TimeoutException:
            print(TimeoutException)


# print(vendors)
url = KILOS

if url == KILOS:
    driver.get(url)
    time.sleep(5)
    searchWithKilo()
elif url == RECON1:
    driver.get(url)
    time.sleep(45)
    searchWithRecon()
