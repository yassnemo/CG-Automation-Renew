import subprocess
import pyautogui
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pygetwindow as gw  # For detecting UAC prompt (optional)

# Function to open CyberGhost using a shortcut (.lnk or .exe)
def open_program():
    shortcut_path = r"C:\Program Files\CyberGhost 8\Dashboard.exe"  # Path to CyberGhost program
    if os.path.exists(shortcut_path):
        subprocess.Popen([shortcut_path])
        print(f"Opened CyberGhost program: {shortcut_path}")
    else:
        print(f"CyberGhost shortcut not found at: {shortcut_path}")

# Function to wait for user to click "Yes" on the UAC prompt
def wait_for_user_to_click_yes():
    print("Please click 'Yes' on the UAC prompt, then press Enter to continue...")
    input("Press Enter to resume once you've handled the UAC prompt.")

# Optional: Wait for the UAC window to disappear automatically
def wait_for_uac_prompt_to_disappear():
    print("Waiting for the UAC prompt to be handled...")
    while True:
        uac_window = [w for w in gw.getAllTitles() if "User Account Control" in w]
        if not uac_window:
            print("UAC prompt has been handled.")
            break
        time.sleep(1)

# Function to automate browser actions and extract an email
def automate_browser():
    driver_path = r"F:\Project\MyAutomationProject\chromedriver.exe"  # Path to ChromeDriver
    if not os.path.exists(driver_path):
        print("ChromeDriver not found!")
        return None

    # Set up the Selenium WebDriver (Chrome)
    driver = webdriver.Chrome(executable_path=driver_path)

    try:
        # Step 1: Go to the email list page
        driver.get("https://emailfake.com/channel7/")  # Email fake channel
        time.sleep(5)  # Wait for the page to load

        # Step 2: Extract the first email from the page
        email_element = driver.find_element(By.CSS_SELECTOR, "div#emails > div > span")  # Update the selector
        email = email_element.text  # Extract email text
        print(f"Extracted email: {email}")

        # Return extracted email to use in CyberGhost automation
        return email

    except Exception as e:
        print(f"Error during browser automation: {e}")
    finally:
        driver.quit()
        print("Browser automation completed.")

# Function to automate CyberGhost account creation
def automate_cyberghost(email):
    time.sleep(5)  # Wait for CyberGhost to load

    # Step 1: Click "Create Account" button
    pyautogui.click(x=100, y=200)  # Adjust (x, y) to the "Create Account" button location
    print("Clicked 'Create Account'.")

    time.sleep(1)

    # Step 2: Fill in the email address
    pyautogui.write(email)
    print(f"Entered email: {email}")

    # Step 3: Re-enter the email in the password field
    pyautogui.press('tab')  # Move to the password field
    pyautogui.write(email)
    print(f"Entered email as password: {email}")

    # Step 4: Confirm the password (re-enter email)
    pyautogui.press('tab')  # Move to the "Confirm Password" field
    pyautogui.write(email)
    print(f"Entered email in confirm password field: {email}")

    # Step 5: Submit the form
    pyautogui.press('tab')  # Move to the "OK" button (if it's a tab-navigable button)
    pyautogui.press('enter')  # Press Enter to submit
    print("Clicked 'OK' to create account.")

    print("Waiting for email confirmation...")
    time.sleep(15)  # Wait for confirmation email to arrive

# Main function to run the script
def main():
    # Step 1: Open CyberGhost program
    open_program()

    # Step 2: Wait for the UAC prompt to be approved
    wait_for_user_to_click_yes()  # Or use wait_for_uac_prompt_to_disappear()

    # Step 3: Automate browser tasks (email extraction)
    email = automate_browser()
    if email is None:
        print("No email extracted. Exiting script.")
        return

    # Step 4: Automate CyberGhost account creation with the extracted email
    automate_cyberghost(email)

if __name__ == "__main__":
    main()
