---
description: This page contains all of the startup options available for Simple Selenium
---

# Startup Options

The following options can be passed to the Simple Selenium WebDriver class:

```python
#Below are all of the startup options for Simple Selenium & their default values
#------------------------------------------------
webdriverName #The browser name to use. Currently supports "chrome", "firefox", & "custom"
headless=False #Runs the webdriver in headless mode if True (makes browser invisible). Read more here: https://www.selenium.dev/blog/2023/headless-is-going-away/ 
maximized=False #Starts the browser maximized if True
custom_driver=None #Allows a custom Selenium webdriver object to be passed in (allows you to pass an unsupported browser or driver with unsupported options to Simple Selenium)
custom_chrome_options=False #Allows you to pass completely custom options from the selenium.webdriver.chrome.options.Options class
custom_firefox_options=False #Allows you to pass completely custom options from the selenium.webdriver.firefox.options.Options class
firefox_binary_location=False #Set a custom path to your FireFox installation (eg. C://users/myuser/path/to/firefox/installation/firefox.exe). Tries to automatically find the binary path if left False
save_profile=False #Save all session data (logins, cookies, etc) in persistent profile. Currently only supported by Chrome
profile_directory=None #Set a custom path to where you want to save persistent profile data. Puts profile data in ./chromeProfileData by default
profile_name=None #Set a name for this profile. Allows you to have multiple isolated profiles with different logins, cookies, etc.
show_selenium_cmd=False #Hides/shows the Selenium webdriver cmd prompt that pops up. Hides it by default
use_proxy=False #Allows use of a proxy
proxy_host=None #The proxy host (eg. 127.0.0.1)
proxy_port=None #The proxy port (eg. 8081)
proxy_username=None #The proxy username (if using user:pass authentication). Currently only supported by Chrome
proxy_password=None #The proxy password (if using user:pass authentication). Currently only supported by Chrome
verbose=False #Whether or not to log non-critical events. Defaults to not logging non-critical events
enable_basic_logging=True #Whether or not to log critical events. Defaults to logging critical events
save_logs_in_file=False #Toggle whether logs should be printed to console or saved to a file. Defaults to logging on console
logging_file_name=None #The logging filename to use for this session. Defaults to logs_{month}-{day}-{year}.{hour}-{minute}-{second}.txt
```

Using startup options:

```python
driver=SimpleSelenium("chrome",maximized=True,save_logs_in_file=True)
#Starts Chrome browser maximized
#Saves all logs to a log file in ./simpleSeleniumLogs/

driver=SimpleSelenium("chrome",use_proxy=True,proxy_host="127.0.0.1",proxy_port="8081",verbose=True)
#Starts Chrome browser with a custom localhost proxy
#Logs non-critical events

driver=SimpleSelenium("firefox",maximized=True)
#Starts FireFox browser maximized

service=Service("./webdriverManager/chromedriver.exe") #from selenium.webdriver.chrome.service import Service
myCustomSeleniumDriver=webdriver.Chrome(service=service) #Initiates custom Selenium webdriver
driver=SimpleSelenium("custom",custom_driver=myCustomSeleniumDriver)
#Creates custom Chrome driver with custom options not supported by Simple Selenium
```

