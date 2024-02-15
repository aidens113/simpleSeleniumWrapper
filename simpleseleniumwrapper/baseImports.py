import time
import os
import sys
import platform
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from subprocess import CREATE_NO_WINDOW
import string
import requests
import io
import zipfile
import re
import warnings
from functools import wraps
import logging
from datetime import datetime

#Error handler that shuts down driver on err
def stop_driver_on_error(method):
    @wraps(method)
    def sub(self, *method_args, **method_kwargs):
        try:
            method(self, *method_args, **method_kwargs)
        except Exception as err:
            logging.error("Killing webdriver")
            if self.driver!=None:
                #Close driver if possible
                self.close()
            raise Exception(err)
    return sub

#Auto-decorator from: https://stackoverflow.com/questions/6307761/how-to-decorate-all-functions-of-a-class-without-typing-it-over-and-over-for-eac - thx (:
def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__: # there's propably a better way to do this
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate
