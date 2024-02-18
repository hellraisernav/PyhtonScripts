import feedparser
import requests

url="https://www.lifehacker.com/rss"

f=feedparser.parse(url)
print(f['title'])