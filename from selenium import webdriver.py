from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager 

username = input('Pl Enter Your Facebook username: ')
passwd = getpass('Enter your Facebook password: ')

#driver = webdriver.Chrome(ChromeDriverManager().install)
driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver')
driver.get('https://www.facebook.com')

txtUsername = driver.find_element_by_id('email')
txtUsername.send_keys(username)

txtPasswd = driver.find_element_by_id('pass')
txtPasswd.send_keys(passwd)

btnLogin = driver.find_element_by_id('u_0_b')
btnLogin.submit()