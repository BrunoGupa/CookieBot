from exponential_growth import exp_growth
from selenium_driver import CookieDriver
import time

FINISH_TIME = 300  # seconds
THRESHOLD_TO_GROW = 60  # Time elapsed to buy the most expensive item
MAX_CLICK_TIME = 20  # seconds

Cookie = CookieDriver()
Cookie.build_driver()


start_init = time.time()
start = time.time()

while True:
    Cookie.cookie_click()
    actual_time = time.time()
    elapsed_time = actual_time - start
    total_elapsed_time = actual_time - start_init
    click_time = exp_growth(total_elapsed_time, THRESHOLD_TO_GROW, MAX_CLICK_TIME)
    if elapsed_time > click_time:
        # Buy Items
        Cookie.buy_most_expensive_item()
        start = time.time()
    if total_elapsed_time > FINISH_TIME:
        print(Cookie.score())
        Cookie.quit()


