from config import keys
from selenium import webdriver
import time


def order(keys):
    start_time = time.time()

    driver = webdriver.Chrome("./chromedriver")
    driver.get(keys["product_url"])

    # add to cart
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

    time.sleep(0.1)

    # go to checkout
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

    # name
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(
        keys["name"]
    )

    # email
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys["email"])

    # telephone
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys["tele"])

    # address
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys["address"])

    # address 2 (apt,unit, etc)
    driver.find_element_by_xpath('//*[@id="oba3"]').send_keys(keys["address_2"])

    # zip code (autofills city and state with this)
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(
        keys["zip_code"]
    )

    # credit card number
    driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys(keys["card_number"])

    # card month
    driver.find_element_by_xpath(
        '//*[@id="credit_card_month"]/option[{}]'.format(keys["exp_month"])
    ).click()

    # card year
    driver.find_element_by_xpath(
        '//*[@id="credit_card_year"]/option[{}]'.format(keys["exp_year"])
    ).click()

    # CVV
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys["CVV"])

    # agree to terms and conditions
    driver.find_element_by_xpath(
        '//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins'
    ).click()

    # proceed to payment
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()

    end_time = time.time()

    exe_time = end_time - start_time
    print("\nExecution Time: {} seconds".format(round(exe_time, 3)))


if __name__ == "__main__":
    order(keys)

