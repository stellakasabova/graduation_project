from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def logIn(username_input, password_input, paths):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://pixabay.com/accounts/login/')

    element1 = driver.find_element(By.NAME, 'username')
    element1.clear()
    element1.send_keys(username_input.get())

    element2 = driver.find_element(By.NAME, 'password')
    element2.clear()
    element2.send_keys(password_input.get())

    driver.find_element(By.NAME, 'login').click()
    driver.get('https://pixabay.com/accounts/media/')

    driver.get('https://pixabay.com/accounts/media/upload/')
    driver.find_element(By.CLASS_NAME, 'dialog-container').find_element(By.NAME, 'ownership').click()
    driver.find_element(By.CLASS_NAME, 'dialog-container').find_element(By.NAME, 'license').click()
    driver.find_element(By.CLASS_NAME, 'dialog-container').find_element(By.CLASS_NAME, 'primary-button').click()

    big_string = paths[0] + '\n' + paths[1] + '\n' + paths[2]
    files = driver.find_element(By.CLASS_NAME, 'dz-hidden-input')
    files.send_keys(big_string)

    time.sleep(30)

    tags = driver.find_elements(By.CLASS_NAME, 'tagify__input')
    print("found")
    for element in tags:
        ActionChains(driver).move_to_element(element)
        element.clear()
        element.send_keys("smth")
        print("in loop")

    time.sleep(40)

def upload(paths):
    upload_window = Toplevel(height=300, width=300)
    username_label = Label(upload_window, text="Username:")
    username_label.pack()
    username_input = Entry(upload_window)
    username_input.pack()

    password_label = Label(upload_window, text="Password: ")
    password_label.pack()
    password_input = Entry(upload_window, show="*")
    password_input.pack()

    upload_func_button = Button(upload_window, text="Upload", command=lambda: logIn(username_input, password_input, paths))
    upload_func_button.pack()

