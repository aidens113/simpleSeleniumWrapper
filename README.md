---
description: Learn how to setup and use Simple Selenium with some basic examples
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# The Basics

## About Simple Selenium

Simple Selenium is a Python wrapper for Selenium that is intended to make browser automation as painless as possible.

## Main Features

* Automatically installs the correct/latest version of chromedriver/geckodriver for your OS & keeps it updated forever.
* Using Chrome with Simple Selenium is almost completely undetectable by anti-bot services like CloudFlare. Simple Selenium automatically sets the best stealth chrome\_options & patches chromedriver to run undetected while web scraping or running general automation tests.
* Converts Selenium functions into easy-to-remember aliases with plenty of added functionality.
* Incorporates classes like ActionChains & Alert directly into the Simple Selenium WebDriver class for maximum ease of access.
* Adds multiple additional element location methods.
* Built-in startup options for Chrome & FireFox (eg. headless, persistent profiles, etc).
* Proxies are fully supported. Chrome in Simple Selenium supports both IP & username:password authentication, FireFox currently only supports IP authentication.

## Early Development & Bug Reports

This module is still in pre-alpha, so you may encounter bugs while using it. Please report any bugs to the GitHub repository: [https://github.com/aidens113/simpleSeleniumWrapper/issues](https://github.com/aidens113/simpleSeleniumWrapper/issues)

**Simple Selenium wrapper is currently only compatible with Windows & Linux. Using this module on other operating systems may result in a substandard or error-prone experience**

***

## How To Install

Using PIP:

```bash
pip install simpleseleniumwrapper
```

## Getting Started With Simple Selenium

Importing Simple Selenium:

```python
from simpleseleniumwrapper import WebDriver as SimpleSelenium
```

Initiating the Simple Selenium WebDriver class:

```python
driver=SimpleSelenium("chrome") #No need to install chromedriver (it's done automatically by Simple Selenium)
```

🎉 Congratulations! You've successfully setup & run Simple Selenium wrapper for the first time.

### Documentation

You can find the full documentation for Simple Selenium here: [https://tesseractcoder.gitbook.io/simple-selenium-wrapper-python](https://tesseractcoder.gitbook.io/simple-selenium-wrapper-python)\
\
GitHub repository link: [https://github.com/aidens113/simpleSeleniumWrapper/tree/main](https://github.com/aidens113/simpleSeleniumWrapper/tree/main)&#x20;
