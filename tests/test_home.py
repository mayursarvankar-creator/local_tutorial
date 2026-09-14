from logging import config

from playwright.sync_api import Page
from playwright.sync_api import expect

def test_home_page_loads(page, app_url):
    page.goto(app_url)

    print(page.title())

    expect(page).to_have_title("mayur Your Store")

