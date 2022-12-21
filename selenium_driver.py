from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class CookieDriver:
    def __init__(self):
        self.cookie = None
        self.driver = None
        self.chrome_driver_path = "/home/bruno/Developer/chromedriver"
        self.URL = "http://orteil.dashnet.org/experiments/cookie/"

    def build_driver(self):
        service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(self.URL)
        self.cookie = self.driver.find_element(By.ID, "cookie")

    def buy_most_expensive_item(self):
        items = {}
        my_money = self.driver.find_element(By.ID, "money")
        my_money = int("".join(my_money.text.split(",")))

        cost_cursor = self.driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
        cost_cursor = int("".join(cost_cursor.text.split(" ")[2].split(",")))
        items["Cursor"] = cost_cursor

        cost_grandma = self.driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
        cost_grandma = int("".join(cost_grandma.text.split(" ")[2].split(",")))
        items["Grandma"] = cost_grandma

        cost_factory = self.driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
        cost_factory = int("".join(cost_factory.text.split(" ")[2].split(",")))
        items["Factory"] = cost_factory

        cost_mine = self.driver.find_element(By.CSS_SELECTOR, "#buyMine b")
        cost_mine = int("".join(cost_mine.text.split(" ")[2].split(",")))
        items["Mine"] = cost_mine

        cost_shipment = self.driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
        cost_shipment = int("".join(cost_shipment.text.split(" ")[2].split(",")))
        items["Shipment"] = cost_shipment

        cost_alchemy = self.driver.find_element(By.XPATH, "//*[@id='buyAlchemy lab']/b")
        cost_alchemy = int("".join(cost_alchemy.text.split(" ")[3].split(",")))
        items["Alchemy lab"] = cost_alchemy

        cost_portal = self.driver.find_element(By.CSS_SELECTOR, "#buyPortal b")
        cost_portal = int("".join(cost_portal.text.split(" ")[2].split(",")))
        items["Portal"] = cost_portal

        cost_time_machine = self.driver.find_element(By.XPATH, "//*[@id='buyTime machine']/b")
        cost_time = int("".join(cost_time_machine.text.split(" ")[3].split(",")))
        items["Time machine"] = cost_time

        attainable_items = {key: value for key, value in items.items() if value <= my_money}
        try:
            max_key = max(attainable_items, key=attainable_items.get)

        except ValueError:
            pass

        else:
            # Click on the attainable more expensive item
            try:
                # Doing click faster couldn't load the page
                max_item = self.driver.find_element(By.ID, f"buy{max_key}")
                max_item.click()
            except:
                pass

    def cookie_click(self):
        self.cookie.click()

    def score(self):
        score_str = self.driver.find_element(By.ID, "cps")
        score_str = score_str.text.split(":")
        return score_str[0], float("".join(score_str[1].split(",")))

    def quit(self):
        self.driver.quit()
