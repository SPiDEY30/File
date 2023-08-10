# Import necessary modules and classes from Selenium and other libraries
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import quote
import os

# Path to the Microsoft Edge WebDriver executable
edge_driver_path = r"C:\Users\TSIHM\.wdm\drivers\edgedriver_win64\msedgedriver.exe"

# Create a dictionary for experimental options to disable logging
experimental_options = {
    "excludeSwitches": ["enable-logging"]
}

# Set the experimental options for the Edge WebDriver
capabilities = DesiredCapabilities.EDGE.copy()
capabilities["ms:edgeOptions"] = experimental_options

# Initialize the Edge WebDriver using the capabilities
driver = webdriver.Edge(executable_path=edge_driver_path, capabilities=capabilities)

# Suppress WebDriverManager logs and messages
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"


# Define a class to add style to terminal text
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Print a stylish header for the program
print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by Aayushman Ojha     *****")
print("*https://github.com/027abhishekojha/WhatsappAutomation ***")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

# Read the message from the message.txt file
f = open("message.txt", "r", encoding="utf8")
message = f.read()
f.close()

# Print the message on the terminal
print(style.YELLOW + '\nThis is your message-\n')
print(style.GREEN + message)
print("\n" + style.RESET)

# Encode the message to be used in the URL
message = quote(message)

# Read phone numbers from the numbers.txt file
numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()

# Get the total number of phone numbers found
total_number = len(numbers)

# Print the total number of phone numbers found
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)

# Define a delay for waiting in between actions
delay = 30

# Instruct the user to sign in to WhatsApp Web and wait for their input
print('Once your browser opens up, sign in to WhatsApp Web.')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)

# Loop through the phone numbers and send the message to each contact
for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
        continue
    print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx + 1), total_number, number) + style.RESET)
    try:
        # Construct the URL for sending the message
        url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message

        # Try sending the message up to three times
        sent = False
        for i in range(3):
            if not sent:
                driver.get(url)
                try:
                    # Wait for the "send" button to be clickable
                    click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                except Exception as e:
                    print(style.RED + f"\nFailed to send message to: {number}, retry ({i + 1}/3)")
                    print("Make sure your phone and computer are connected to the internet.")
                    print("If there is an alert, please dismiss it." + style.RESET)
                else:
                    sleep(1)
                    click_btn.click()
                    sent = True
                    sleep(3)
                    print(style.GREEN + 'Message sent to: ' + number + style.RESET)
    except Exception as e:
        print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)

# Close the browser after sending all messages
driver.close()
