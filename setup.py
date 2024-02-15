from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

version = '0.0.6'
description = 'An easy-to-use wrapper for Selenium in Python. This package is intended to make writing web automation software in Python as painless as possible!'

# Setting up
setup(
    name="simpleseleniumwrapper",
    version=version,
    author="Aiden S",
    #author_email="<test@gmail.com>",
    description=description,
    #long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['selenium>=4.0'],
    keywords=['python', 'selenium', 'automation', 'wrapper', 'chromedriver','geckodriver','undetected','webdriver','manager'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Operating System Kernels :: Linux",
        "Operating System :: Microsoft :: Windows",
    ]
)
