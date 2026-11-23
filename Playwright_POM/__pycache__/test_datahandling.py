import json
from playwright.sync_api import sync_playwright

def test_jsonHandling():
  with open('testdata/creds.json') as data:
    creds = json.load(data)
    print(creds)
