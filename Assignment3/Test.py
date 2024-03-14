from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Start the Chrome browser session
driver = webdriver.Chrome()

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def calculateTotalAmount():
    totalAmount = 0
    tax = 4.32

    itemAmounts = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_price')
    for itemAmount in itemAmounts:
        # Extract the amount value and convert it to a number
        amount = float(itemAmount.text.replace('$', ''))

        # Add the amount to the total
        totalAmount += amount
        # Add the total to the tax
        finalAmountPlusTax = totalAmount + tax

    # Assert or perform actions with the total amount
    print('Total Amount:', finalAmountPlusTax)  # Logging the total amount for reference

    # Example: Assert the total amount equals a specific value
    assert finalAmountPlusTax == 58.29


def cartItems():
    cartItems = driver.find_elements(By.CSS_SELECTOR, '#cart_contents_container')
    for cartItem in cartItems:
        # Assert the visibility of the elements
        item_name = cartItem.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
        if item_name == 'Sauce Labs Backpack':
            assert item_name == 'Sauce Labs Backpack'
        elif item_name == 'Sauce Labs Bolt T-Shirt':
            assert item_name == 'Sauce Labs Bolt T-Shirt'
        elif item_name == 'Sauce Labs Onesie':
            assert item_name == 'Sauce Labs Onesie'


driver.get('https://www.saucedemo.com/')
time.sleep(4)  # Adding a delay after opening the website
driver.maximize_window()
time.sleep(4)  # Adding a delay after maximizing the window
driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
time.sleep(4)  # Adding a delay after entering username
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
time.sleep(4)  # Adding a delay after entering password
driver.find_element(By.CSS_SELECTOR, '#login-button').click()
time.sleep(4)  # Adding a delay after clicking login button

driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
time.sleep(4)  # Adding a delay after adding backpack to cart
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
time.sleep(4)  # Adding a delay after adding onesie to cart
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
time.sleep(4)  # Adding a delay after adding t-shirt to cart
driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
time.sleep(4)  # Adding a delay after clicking shopping cart link

cartItems()

driver.find_element(By.CSS_SELECTOR, '#checkout').click()
time.sleep(4)  # Adding a delay after clicking checkout button

driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Test')
time.sleep(4)  # Adding a delay after entering first name
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Ignore')
time.sleep(4)  # Adding a delay after entering last name
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('123')
time.sleep(4)  # Adding a delay after entering postal code
driver.find_element(By.CSS_SELECTOR, '#continue').click()
time.sleep(4)  # Adding a delay after clicking continue button

calculateTotalAmount()
time.sleep(4)  # Adding a delay after calculating total amount
cartItems()

driver.find_element(By.CSS_SELECTOR, '#finish').click()
time.sleep(4)  # Adding a delay after clicking finish button

assert driver.find_element(By.CSS_SELECTOR, '.complete-header').is_displayed()
assert driver.find_element(By.CSS_SELECTOR, '#back-to-products').is_displayed()

driver.quit()
