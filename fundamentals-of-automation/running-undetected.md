---
description: >-
  Learn all about how you can do web scraping or automation testing, without
  looking like a bot
---

# Running Undetected

### Introduction

Most websites don't like bots. Unfortunately bots that spam websites, grab private info, commit fraud, and do other black-hat activities give all bots a bad name. For this reason, many websites try to completely stop bots from accessing their websites with services like CloudFlare or ReCaptcha.&#x20;

But not all bots are bad! Some bots run automated web browsers for the good of the public, such as search engines, white-hat vulnerability scanners, and open-source data projects. So on this page you're going to learn how to scrape websites in a responsible manner, while going completely undetected!

### Acting Like a Human

It's important to make your bot look like just another human user to the website you are automating/scraping data from. That mainly includes not visiting too many pages too quickly, or making too many network requests to the target website too quickly.

Some other techniques for avoiding detection are:

* Adding randomized delays when interacting with the target website. Humans don't wait 2.5 seconds every time they visit a page on a website, so your bot shouldn't either
* Avoiding "high-security" areas of a website. Login/register pages, pages that contain sensitive info such as emails, names, phone numbers, etc. tend to be more strict when it comes to automation
* Scraping data that is behind a login/pay wall. In some cases it may even be illegal to scrape information that is behind a login or pay wall, so it's best to only scrape information that can be publicly accessed from the internet. Be sure to research applicable laws in your area regarding web scraping & automation before starting a project.

### Optimal Simple Selenium Startup Options

When scraping with Selenium (or Simple Selenium), there are a few tips that can help you prevent detection.&#x20;

#### Headless Mode

For instance, using headless mode on any browser can be a dead giveaway to websites that your browser is automated:

```python
driver=SimpleSelenium("chrome",headless=False) #Optimal

driver=SimpleSelenium("chrome",headless=True) #Not recommended. Much easier for websites to detect
```

#### Browser Fingerprint

Anti-bot services often identify bots through a browser's "fingerprint". Which is a combination of things like the operating system, browser (chrome, firefox, etc), user agent, IP address, WebRTC properties, cookies, and much more.&#x20;

Simple Selenium automatically removes the most suspicious fingerprint attributes (if you're using Chrome). If you decide to use another browser like FireFox, you'll have to provide custom options to bypass anti-bot services:

```python
driver=SimpleSelenium("chrome") #Optimal

from selenium.webdriver.firefox.options import Options as firefoxOptions
my_custom_options=firefoxOptions()
#Add a bunch of custom options to try and evade detection
driver=SimpleSelenium("firefox",custom_firefox_options=my_custom_options) #Not recommended. Finding the right combo of custom options can be VERY time consuming
```

#### IP Address Quality

Low quality IPs are a major factor when it comes to detecting bots. Services like CloudFlare will "blacklist" your IP for a period of time if you're exhibiting bot-like behavior or spamming requests too fast. When this happens, you can be blocked from visiting all websites that use the same anti-bot detection software for a period of time.

This can be a major problem when scraping a large amount of data, which is where proxies come in:

```python
#Using proxies in Simple Selenium
driver=SimpleSelenium("chrome",use_proxy=True,proxy_host="127.0.0.1",proxy_port="8081",proxy_username="test",proxy_password="test")
```

Much like your browser, anti-bot services can often detect lower quality proxies based on their "fingerprint". So if you end up using proxies for a project, use high quality residential or 4g/5g phone proxies (more expensive) for strict websites, and data-center (much cheaper) proxies for less strict websites.

#### Window Size

Another less conspicuous tell, is your browser's window size. Bots are more likely to run a webdriver in the default size/resolution, humans are much more likely to run their browser maximized.&#x20;

```python
driver=SimpleSelenium("chrome",maximized=True) #Optimal

driver=SimpleSelenium("chrome",maximized=False) #Some websites may flag you as a bot
```

#### Persistent Profiles

Using persistent profiles can be a great way to avoid detection. Bots are more likely to use default browser setups. No customization, no extensions. Persistent profiles store things like cookies & extensions, which can be good (or bad) when scraping websites that share anti-bot platforms:

```python
driver=SimpleSelenium("chrome",save_profile=True,profile_name="myAwesomeProfile")
#Saves all user settings, cookies, history, and extensions to the myAwesomeProfile profile, completely isolated from any other profile name
```

If your bot consistently exhibits human-like behavior, and has browser extensions/customization, anti-bot services & captchas are more likely to let you through without asking if you're human.&#x20;

On the other hand, if your bot constantly spams user actions or visits pages unnaturally fast, you'll be blocked way more often.

#### User Actions

Part of acting like a human is moving the mouse & entering keyboard inputs like a human. This can be a big problem for Selenium (or Simple Selenium), as many Selenium interaction functions (like `.click()` or .`send_keys()`) are a red flag for some anti-bot services.

Simple Selenium currently offers randomized typing & the pure JS version of `.click()`, which makes this module less detectable. In the future, Simple Selenium plans to completely eliminate detectable user action methods.&#x20;

A good solution that you can implement, is completing as few user input actions as possible & using randomized delays between user interactions.&#x20;

### Takeaway

When building automation scripts, the best way to avoid detection is by asking yourself what a human would do on a website, and comparing it to what your bot is actually doing. The more your bot blends in with other users, the better off you'll be.&#x20;
