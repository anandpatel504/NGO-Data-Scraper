# Indian NGOs donate data scraper

In this project, I have scraped the data all of the Indian NGOs that donate funds certified by **GiveIndia** 
`https://www.giveindia.org/certified-indian-ngos` according to their location, and I have stored all the data state wise in the `scrape_indian_ngo_data.json` file.

## Requirements

## BeautifulSoup

Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. If you're using Linux based OS, you can install BeautifulSoup using following command in terminal.

Here, pip is a package-management system used to install and manage software packages written in Python.

```
sudo apt-get update && sudo apt-get install python3-pip
pip3 install beautifulsoup4
```
After finishing the installation process above, you can run the task, using `python3 scrape_indian_ngo_data.py`
