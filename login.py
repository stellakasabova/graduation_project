from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

root = Tk()
root.geometry("100x100")

def logIn(input1, input2):
    username = input1.get()
    password = input2.get()

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://pixabay.com/accounts/login/')

    element1 = driver.find_element(by=By.NAME, value='username')
    element1.clear()
    element1.send_keys(username)

    element2 = driver.find_element(by=By.NAME, value='password')
    element2.clear()
    element2.send_keys(password)

    driver.find_element(by=By.NAME, value='login').click()
    driver.get('https://pixabay.com/accounts/media/')

    driver.get('https://pixabay.com/accounts/media/upload/')
    driver.find_element(by=By.CLASS_NAME, value='dialog-container').find_element(by=By.NAME, value='ownership').click()
    driver.find_element(by=By.CLASS_NAME, value='dialog-container').find_element(by=By.NAME, value='license').click()
    driver.find_element(by=By.CLASS_NAME, value='dialog-container').find_element(by=By.CLASS_NAME, value='primary-button').click()

    files = driver.find_element(by=By.CLASS_NAME, value='dz-hidden-input')
    files.send_keys('D:/photos/Upload/IMG_0386.JPG\nD:/photos/Upload/IMG_0389.png')
    files.submit()

def upload():
    upload_window = Toplevel(height=300, width=300)
    username_label = Label(upload_window, text="Username:")
    username_label.pack()
    username_input = Entry(upload_window)
    username_input.pack()

    password_label = Label(upload_window, text="Password: ")
    password_label.pack()
    password_input = Entry(upload_window, show="*")
    password_input.pack()

    upload_func_button = Button(upload_window, text="Upload", command=lambda: logIn(username_input, password_input))
    upload_func_button.pack()

bttn = Button(root, text="upload", command=upload).grid(row=0, column=0)

root.mainloop()
