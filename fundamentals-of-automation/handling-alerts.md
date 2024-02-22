---
description: On this page you'll learn how to handle alerts with Simple Selenium
---

# Handling Alerts

### Introduction

Sometimes when building automation scripts, you'll need to deal with popup alerts. Handling alerts with Simple Selenium is dead simple, which you'll learn all about on this page.

### Simple Selenium Alerts

Interacting with alerts in Simple Selenium is simple. See the example below, which visits an alert test page & handles the alert:

```python
#Start chrome webdriver with custom options
driver=SimpleSelenium("chrome",save_profile=True,profile_name="myAwesomeProfile",save_logs_in_file=True,maximized=False)

#Visit Alert Test Page
driver.visit("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

#Waits 2 seconds
time.sleep(2)

#Clicks "Show Prompt Box" btn
driver.by_id('promptexample').click()

#Waits 1 second
time.sleep(1)

#You can access the Alerts class with driver.alerts

#Writes text to alert box
driver.alerts.write("Some text to type")

#Accepts alert box
driver.alerts.accept()

```

### List of All Alert Functions

Below, are a list of all alert-based functions that Simple Selenium offers.

#### Accept Alert Box

To accept an alert box:

```python
driver.alerts.accept() #Accepts alert box

#Default options:
retry_if_fail=True #Whether or not to retry if handling alert fails
max_retries=5 #Max number of retries before returning False (if retry_if_fail==True)
delay_for_each_retry=1 #Time delay between each retry in seconds (if retry_if_fail==True)

driver.alerts.accept(retry_if_fail=False) #Doesn't retry if initial attempt to handle alert fails
```

#### Dismiss Alert Box

To dismiss an alert box:

```python
driver.alerts.dismiss() #Accepts alert box

#Default options:
retry_if_fail=True #Whether or not to retry if handling alert fails
max_retries=5 #Max number of retries before returning False (if retry_if_fail==True)
delay_for_each_retry=1 #Time delay between each retry in seconds (if retry_if_fail==True)

driver.alerts.dismiss(retry_if_fail=False) #Doesn't retry if initial attempt to handle alert fails
```

#### Write To Alert Box

To write text to an alert box:

```python
driver.alerts.write("Text to write") #Writes text to an alert box

#Default options:
retry_if_fail=True #Whether or not to retry if handling alert fails
max_retries=5 #Max number of retries before returning False (if retry_if_fail==True)
delay_for_each_retry=1 #Time delay between each retry in seconds (if retry_if_fail==True)

driver.alerts.write("Text to write",retry_if_fail=False) #Doesn't retry if initial attempt to handle alert fails
```
