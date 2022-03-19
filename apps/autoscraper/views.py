from django.shortcuts import render
from autoscraper import AutoScraper
from .models import Scraper

def scraper(url, wanted_list):
    url = str(input("Enter a url: "))
    wanted_list = list(input("Enter some keywords"))
    scraper = AutoScraper()
    result = scraper.build(url, wanted_list)
    return result
